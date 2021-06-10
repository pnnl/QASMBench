# ----------------------------------------------------------------------
# QASMBench: A Low-level OpenQASM Benchmark Suite
# ----------------------------------------------------------------------
# Samuel Stein, Ang Li
# Pacific Northwest National Laboratory(PNNL), U.S.
# BSD Lincese.
# Created 06/10/2021.
# PNNL IPID: 31924-E, IR: PNNL-SA-153380, PNNL-SA-162867, ECCN:EAR99
# ----------------------------------------------------------------------


from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit.compiler import *
from qiskit.providers.aer import AerProvider,AerSimulator,QasmSimulator
import re
import numpy as np
import matplotlib.pyplot as plt
import itertools

# Metrics required for QASM Bench:
# - Binary matrix representing circuit
# - Depth of each Qubit (Number of operations on each qubit)
# - Number of Qubits in the circuit
# - Number of 2-Qubit gates
# - Number of measurements
# - Number of 1-Qubit gates

class QASMetric():
    def __init__(self,qasm):
        self.qasm = qasm

        # =======  Global tables and variables =========

        # Starndard gates are gates defined in OpenQASM header.
        # Dictionary in {"gate name": number of standard gates inside}
        self.STANDARD_GATE_TABLE = {
            "r": 1,   # 2-Parameter rotation around Z-axis and X-axis
            "u3": 1,  # 3-parameter 2-pulse single qubit gate
            "u2": 1,  # 2-parameter 1-pulse single qubit gate
            "u1": 1,  # 1-parameter 0-pulse single qubit gate
            "cx": 1,  # controlled-NOT
            "id": 1,  # idle gate(identity)
            "x": 1,  # Pauli gate: bit-flip
            "y": 1,  # Pauli gate: bit and phase flip
            "z": 1,  # Pauli gate: phase flip
            "h": 1,  # Clifford gate: Hadamard
            "s": 1,  # Clifford gate: sqrt(Z) phase gate
            "sdg": 1,  # Clifford gate: conjugate of sqrt(Z)
            "t": 1,  # C3 gate: sqrt(S) phase gate
            "tdg": 1,  # C3 gate: conjugate of sqrt(S)
            "rx": 1,  # Rotation around X-axis
            "ry": 1,  # Rotation around Y-axis
            "rz": 1,  # Rotation around Z-axis
            "c1": 1,  # Arbitrary 1-qubit gate
            "c2": 1}  # Arbitrary 2-qubit gate

        # Composition gates are gates defined in OpenQASM header.
        # Dictionary in {"gate name": number of standard gates inside}
        self.COMPOSITION_GATE_TABLE = {
            "p":1, # Phase Gate
            "cz": 3,  # Controlled-Phase
            "cy": 3,  # Controlled-Y
            "swap": 3,  # Swap
            "ch": 11,  # Controlled-H
            "ccx": 15,  # C3 gate: Toffoli
            "cswap": 17,  # Fredkin
            "crx": 5,  # Controlled RX rotation
            "cry": 4,  # Controlled RY rotation
            "crz": 4,  # Controlled RZ rotation
            "cu1": 5,  # Controlled phase rotation
            "cu3": 5,  # Controlled-U
            "rxx": 7,  # Two-qubit XX rotation
            "ryy": 7,
            "rzz": 3,  # Two-qubit ZZ rotation
            "rccx": 9,  # Relative-phase CCX
            "rc3x": 18,  # Relative-phase 3-controlled X gate
            "c3x": 27,  # 3-controlled X gate
            "c3sqrtx": 27,  # 3-controlled sqrt(X) gate
            "c4x": 87  # 4-controlled X gate

        }

        # OpenQASM native gate table, other gates are user-defined.
        self.GATE_TABLE = {**self.COMPOSITION_GATE_TABLE, **self.STANDARD_GATE_TABLE}

        # ==================================================================================
        # For the statistics of the number of CNOT or CX gate in the circuit

        # Number of CX in Standard gates
        self.STANDARD_CX_TABLE = {"r": 0,"u3": 0, "u2": 0, "u1": 0, "cx": 1, "id": 0, "x": 0, "y": 0, "z": 0, "h": 0,
                             "s": 0, "sdg": 0, "t": 0, "tdg": 0, "rx": 0, "ry": 0, "rz": 0, "c1": 0, "c2": 1}
        # Number of CX in Composition gates
        self.COMPOSITION_CX_TABLE = {"p":0,"cz": 1, "cy": 1, "swap": 3, "ch": 2, "ccx": 6, "cswap": 8, "crx": 2, "cry": 2,
                                "crz": 2, "cu1": 2, "cu3": 2, "rxx": 2, "rzz": 2, "ryy":2, "rccx": 3, "rc3x": 6, "c3x": 6,
                                "c3sqrtx": 6,
                                "c4x": 18}

        self.CX_TABLE = {**self.STANDARD_CX_TABLE, **self.COMPOSITION_CX_TABLE}

        self.USER_DEFINED_GATES = {}
        # Keywords in QASM that are currently not used
        self.other_keys = ["measure", "barrier", "OPENQASM", "include", "creg", "if", "reset"]
        self.measure_key = "measure"
        self.trigger_key = 'if'
        self.skip_keys = ["OPENQASM","include", "qreg", "creg","barrier", "reset","//"]
        # To register and look-up user-defined function in QASM
        # Format: {"function_name": gate_num}
        function_table = {}
        # Format: {"function_name": cx_gate_num}
        cx_table = {}
        self.collate_gates()
        self.preprocess_qasm()
        self.get_gate_count()
        self.get_dual_qubit_gate_count()
        self.get_single_qubit_gate_count()
        self.get_total_gate_count()
        self.get_qubit_depths()
        self.get_maximum_qubit_depth()
        self.get_circuit_matrix()
        self.get_max_dual_qubit_depth()

    def evaluate_qasm(self):
        self.get_circuit_matrix_timed()
        self.calc_operation_density()
        self.calc_measurement_density()
        self.calc_fdm()
        self.calc_size_factor()
        self.calc_entanglement_variance()
        print('-'*10+'Baseline Metrics'+'-'*10)
        print(f'Qubit Count: {self.qubit_count}')
        print(f'Maximum Qubit Depth: {self.max_qubit_depth}')
        print(f'Maximum Qubit Depth ID: {self.max_qubit_depth_id}')
        print(f'Single Gate Count: {self.single_gate_count}')
        print(f'Dual Gate Count: {self.dual_gate_count}')
        print('-'*10+'Calculated Metrics'+'-'*10)
        print(f"Operation Density: {self.operation_density:.3f}\n"
              f"FDM: {self.fdm:.3f}\n"
              f"Measurement Ratio: {self.measurement_ratio:.3f}\n"
              f"Entanglement Variance : {self.entanglement_variance:.3f}\n")
        return {'qubit_count':self.qubit_count,
                # Circuit depth is defined in calculations below, therefore we need not a function, same as width
                'circuit_depth':self.depth,
                'circuit_width':self.qubit_count,
                'retention_lifespan':self.fdm,
                'gate_density':self.operation_density,
                'dual_gate_count':self.dual_gate_count,
                'measurement_density':self.measurement_ratio,
                'size_factor':self.size_factor,
                'gate_count':self.total_gate_count,
                'entanglement_variance':self.entanglement_variance,
                'circuit_depth': self.circ_matrix.shape[1]}

    # Metric Definitions:
    # ----------------------------
    # Calculate Gate Density,
    # ----------------------------
    def calc_operation_density(self):
        circuit_area =self.circ_matrix.shape[0]*self.circ_matrix.shape[1]
        self.operation_density = (self.single_gate_count + 2*self.dual_gate_count)/(self.depth*self.qubit_count)

    # ----------------------------
    # Calculate Measurement Density,
    # ----------------------------
    def calc_measurement_density(self):
        self.measurement_ratio = np.log(self.circ_matrix.shape[0]*self.depth)/self.measurement_count

    # ----------------------------
    # Calculate Retention Lifespan
    # ----------------------------
    def calc_fdm(self):
        self.fdm = np.log(self.depth)

    def calc_size_factor(self):
        self.size_factor = np.log(self.gate_count)

    # ----------------------------
    # Calculate Quantum Area
    # ----------------------------
    def calc_quantum_area(self):
        self.application_time = self.circ_matrix.shape[1]
        self.quantum_area = self.application_time*self.qubit_count

    # ----------------------------
    # Calculate described entanglement variance from QASMBench
    # ----------------------------
    def calc_entanglement_variance(self):
        avg_cnot = 2*self.dual_gate_count/self.qubit_count
        print(self.dual_gate_count)
        print(self.dual_gate_count_id)
        numerator = 0
        for value in list(self.dual_gate_count_id.values()):
            numerator += np.square(value-avg_cnot)
        numerator = np.log(numerator+1)
        self.entanglement_variance = numerator/self.qubit_count

    # ----------------------------
    # Return the gate performed in
    # a QASM operation.
    # ----------------------------
    def get_op(self,line):
        if line.find("(") != -1:
            line = line[:line.find("(")].strip()
        op = line.split(" ")[0].strip()
        return op

    # ----------------------------
    # Return the  ID's
    # in a operation
    # ----------------------------
    def get_qubit_id(self,line):
        line = line.strip(';')
        op_qubits = line.split(" ")[1].strip().split(',')
        qubit_ids = []
        for op_qubit in op_qubits:
            if '[' in op_qubit:
                qubit_prefix = op_qubit.split('[')[0]
                num = int(re.findall('^.*?\[[^\d]*(\d+)[^\d]*\].*$',op_qubit)[0])
                qubit_ids.append(qubit_prefix+str(num))
            else:
                qubit_ids = [x for x in self.qubit_labelled.keys() if op_qubit in x]
        return qubit_ids

    def collate_gates(self):
        gate_def = "gate"
        temporary_qasm = np.array([x.strip() for x in self.qasm.split('\n')])
        start_point,end_point = None,None
        to_remove = []
        for index,line in enumerate(temporary_qasm):
            line_contents = line.split(' ')
            if line_contents[0].strip() == gate_def:
                start_point = index
                gate_name = line_contents[1]
                qubit_count = len(line_contents[2].split(','))
            if line_contents[0].strip() == '}':
                end_point = index
            if start_point and end_point:
                gate_count = 0
                cx_count = 0
                for i in range(end_point-start_point-1):
                    print(temporary_qasm[start_point+i+1])
                    if '{' in temporary_qasm[start_point+i+1]:
                        continue
                    operation = self.get_op(temporary_qasm[start_point+i+1])
                    cx_count += self.CX_TABLE[operation]
                    gate_count += self.GATE_TABLE[operation]
                to_remove.append((start_point,end_point))
                end_point,start_point=None,None
                self.CX_TABLE[gate_name]=cx_count
                self.GATE_TABLE[gate_name]=gate_count
        valid_indexes = np.ones(len(temporary_qasm))
        for start,end in to_remove:
            valid_indexes[start:end+1] = 0
        temporary_qasm = temporary_qasm[valid_indexes.astype('bool')]
        self.qasm = temporary_qasm



    def preprocess_qasm(self):
        qreg = "qreg"
        creg = "creg"
        regex_str = '^.*?\[[^\d]*(\d+)[^\d]*\].*$'
        regex_id_str = '(.*?)\s*\['
        # Break QASM into line by line commands
        qasm = self.qasm
        # Search for all qubit declaration lines
        qubit_count = [x for x in qasm if qreg in x]
        t_qubits = 0
        t_cbits = 0
        qbit_labelled = {}
        # Load all qubits into the qubit count and give them unique IDs
        for qubit_index in qubit_count:
            info_string = qubit_index.split(' ')[-1]
            qubit_id = re.findall(regex_id_str, info_string)[0]
            qbit_counts= int(re.findall(regex_str, qubit_index)[0])
            try:
                previous_cap = max(qbit_labelled.values()) +1
            except:
                previous_cap = 0
            for i in range(qbit_counts):
                qbit_labelled[str(qubit_id)+str(i)] = i + previous_cap
            t_qubits +=int(qbit_counts)
        # Search for all cbit declaration lines

        cbit_count = [x for x in qasm if creg in x]
        cbit_labelled = {}
        # Load all cbits into the cbit count and give them unique IDs
        for cbit_index in cbit_count:
            info_string = cbit_index.split(' ')[-1]
            cbit_id = re.findall(regex_id_str,info_string)[0]
            cbit_counts= int(re.findall(regex_str, cbit_index)[0])
            for i in range(cbit_counts):
                if len(cbit_labelled)==0:
                    cbit_labelled[str(cbit_id)+str(i)]=i
                else:
                    cbit_labelled[str(cbit_id)+str(i)]=i+max(cbit_labelled.values())
            t_cbits +=int(cbit_counts)
        # Remove all If statements from the QASM code, as we count these as gates.
        for i,line in enumerate(qasm):
            if self.trigger_key in line[:3]: # Fix this later - IF causes problems
                indx = line.find(' ')
                line = line[indx+1:]
                qasm[i] = line
        filtered_qasm = [x for x in qasm if not any(skip_key in x for skip_key in self.skip_keys)]
        filtered_qasm = [x for x in filtered_qasm if x != '']  # Drop any trailing end of lists such as ''
        measurement_count = len([x for x in filtered_qasm if self.measure_key in x])
        filtered_qasm = [x for x in filtered_qasm if not self.measure_key in x]
        self.measurement_count = measurement_count
        # Filter the QASM code for all lines containing strings within the "SKIP Keys" variable
        self.qubit_count = int(t_qubits)
        self.cbit_count = int(t_cbits)
        self.qubit_labelled = qbit_labelled
        self.cbit_labelled = cbit_labelled
        self.processed_qasm = filtered_qasm

    def get_gate_count(self):
        count = 0
        for gate in self.processed_qasm:
            n_qubits = len(self.get_qubit_id(gate))
            op = self.get_op(gate)
            if op not in self.GATE_TABLE:
                print(f"{op} not counted towards evaluation. Not a valid from default gate tables")
                continue
            else:
                count += self.GATE_TABLE[op]*n_qubits
        self.gate_count = count

    def get_measure_count(self,qasm_list):
        count = 0
        for gate in qasm_list:
            op = self.get_op(gate)
            if op in self.measure_key:
                count += 1
        self.measure_count = count

    def get_dual_qubit_gate_count(self):
        count = 0
        self.dual_gate_count_id = {}
        for gate in self.processed_qasm:
            n_qubits = len(self.get_qubit_id(gate))
            qubit_id = self.get_qubit_id(gate)
            op = self.get_op(gate)
            if op not in self.CX_TABLE:
                print(f"{op} not counted towards evaluation. Not a valid from default gate tables")
                continue
            else:
                count += self.CX_TABLE[op]
            for qb in qubit_id:
                if self.qubit_labelled[qb] not in self.dual_gate_count_id:
                    self.dual_gate_count_id[self.qubit_labelled[qb]] = 0
                self.dual_gate_count_id[self.qubit_labelled[qb]] += self.CX_TABLE[op]
        self.dual_gate_count = count

    def get_dual_qubit_id_gate_count(self,qubit_id):
        count = 0
        for gate in self.processed_qasm:
            op = self.get_op(gate)
            if op not in self.CX_TABLE:
                print(f"{op} not counted towards evaluation. Not a valid from default gate tables")
                continue
            if qubit_id not in self.get_qubit_id(gate):
                continue
            count += self.CX_TABLE[op]
        return count

    def get_single_qubit_gate_count(self):
        count = 0
        for gate in self.processed_qasm:
            n_qubits = len(self.get_qubit_id(gate))
            op = self.get_op(gate)
            if op not in self.GATE_TABLE:
                print(f"{op} not counted towards evaluation. Not a valid from default gate tables")
                continue
            else:
                count += n_qubits*(self.GATE_TABLE[op] - self.CX_TABLE[op])
        self.single_gate_count = count

    def get_qubit_depths(self):
        qubit_depth = {}
        for gate in self.processed_qasm:
            op = self.get_op(gate)
            if op not in self.GATE_TABLE:
                print(f"{op} not counted towards evaluation. Not a valid from default gate tables")
                continue
            else:
                qubit_id = self.get_qubit_id(gate)
                for qubit in qubit_id:
                    if qubit not in qubit_depth.keys():
                        qubit_depth[qubit] = 0
                    qubit_depth[qubit] += 1
        self.qubit_depth = qubit_depth

    def get_maximum_qubit_depth(self):
        self.get_qubit_depths()
        qubit_depths = self.qubit_depth
        max_value = max(qubit_depths.values())  # maximum value
        max_keys = [k for k, v in qubit_depths.items() if v == max_value][0]
        # getting all keys containing the `maximum`
        self.max_qubit_depth_id = max_keys
        self.max_qubit_depth = max_value
        return max_keys, max_value

    def get_total_gate_count(self):
        self.total_gate_count = self.dual_gate_count + self.single_gate_count

    def get_max_dual_qubit_depth(self):
        self.max_dual_qubit_count = self.get_dual_qubit_id_gate_count(self.max_qubit_depth_id)

    def get_circuit_matrix_timed(self):
        circ_matrix = np.zeros(shape=(self.qubit_count, self.gate_count))
        time = 0
        for gate in self.processed_qasm:
            time_reverse = 0
            op = self.get_op(gate)
            qubit_ids = self.get_qubit_id(gate)
            for qubit_id in qubit_ids:
                if circ_matrix[self.qubit_labelled[qubit_id], time] > 0:
                    time += 1
                    break
            # Push back to nearest time if it is a single qubit operation
            app_indx = []
            for qubit_id in qubit_ids:
                for i in range(2 * self.max_qubit_depth):
                    x = np.sum(circ_matrix[self.qubit_labelled[qubit_id], time - i:time])
                    if x >= 1:
                        app_indx.append(i - 1)
                        break
            try:
                time_reverse = np.min(app_indx)
            except:
                time_reverse = 0
            for qubit_id in qubit_ids:
                circ_matrix[self.qubit_labelled[qubit_id], time - time_reverse] = self.GATE_TABLE[op]
        size = circ_matrix.shape[1] - 1
        inv_size = 0
        for i in range(1, size):
            if np.sum(circ_matrix[:, -i]) == 0:
                continue
            elif np.sum(circ_matrix[:, -i]) > 0:
                inv_size = i - 1
                break
        if inv_size != 0:
            circ_matrix = circ_matrix[:, :-inv_size]
        self.circ_matrix_timed = circ_matrix
        depth = 0
        for i in range(circ_matrix.shape[1]):
            depth += np.max(circ_matrix[:,i])
        self.depth = depth


    def get_circuit_matrix(self):
        #2*n+3 is arbitrary, +3 incase it is very small, and 2* to compensate
        circ_matrix = np.zeros(shape=(self.qubit_count, self.gate_count))
        time = 0
        for gate in self.processed_qasm:
            time_reverse = 0
            op = self.get_op(gate)
            qubit_ids = self.get_qubit_id(gate)
            for qubit_id in qubit_ids:
                if circ_matrix[self.qubit_labelled[qubit_id], time] == 1:
                    time += 1
                    break
            # Push back to nearest time if it is a single qubit operation
            app_indx = []
            for qubit_id in qubit_ids:
                for i in range(2 * self.max_qubit_depth):
                    x = np.sum(circ_matrix[self.qubit_labelled[qubit_id], time - i:time])
                    if x >= 1:
                        app_indx.append(i - 1)
                        break
            try:
                time_reverse = np.min(app_indx)
            except:
                time_reverse = 0
            for qubit_id in qubit_ids:
                circ_matrix[self.qubit_labelled[qubit_id], time - time_reverse] = 1
        size = circ_matrix.shape[1] - 1
        inv_size = 0
        for i in range(1, size):
            if np.sum(circ_matrix[:, -i]) == 0:
                continue
            elif np.sum(circ_matrix[:, -i]) > 0:
                inv_size = i - 1
                break
        if inv_size != 0:
            circ_matrix = circ_matrix[:, :-inv_size]
        self.circ_matrix = circ_matrix
