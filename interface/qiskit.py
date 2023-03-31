import os
from qiskit import QuantumCircuit, transpile

class QASMBenchmark:
    """
    A class for managing a collection of QASM circuits for benchmarking.
    The interface can behave like a iterator, a list, or a dict.

    Examples:
    
        Initiate the object:

        .. code-block::

            # path to the root directory of QASMBench
            path = "path/to/the/root/of/QASMBench"

            # selected category for QASMBench
            category = "small" 

            # select only the circuits with the number of qubits in the list
            num_qubits_list = list(range(3, 5))

            # whether to remove the final measurement in the circuit
            remove_final_measurements = True

            # whether use qiskit.transpile() to transpile the circuits (note: must provide qiskit backend)
            do_transpile = False

            # arguments for qiskit.transpile(). backend should be provide at least
            transpile_args = {}
            
            bm = QASMBenchmark(path, category, num_qubits_list=num_qubits_list, remove_final_measurements=remove_final_measurements, do_transpile=do_transpile, **transpile_args)
        
        Retrieve Circuits:

        1. Behave like a iterator:
        
        .. code-block::

            circ_1 = next(bm)
            circ_2 = next(bm)

        2. Behave like a list:

        .. code-block::

            circ = bm[0]
            circ_list = bm[:2]
        
        3. Behave like a dict:

        .. code-block::

            circ = bm.get("teleportation_n3")
            circ_list = bm.get(["teleportation_n3", "adder_n4"])

        
        
        Get information of the benchmark:

        .. code-block::

            # the list of all circuits
            circ_list = bm.circ_list

            # the list of all circuit names
            circ_list = bm.circ_name_list

            # return the length of the benchmark
            bm_length = len(bm)


    Args:
        path (str): The directory path containing the QASM files.
        category (str): The category of circuits in the directory.
        num_qubits_list (int or list, optional): The number of qubits to filter the circuits by. Defaults to None.
        remove_final_measurements (bool, optional): Whether or not to remove the final measurements from each circuit. Defaults to False.
        do_transpile (bool, optional): Whether or not to transpile each circuit. Defaults to False.
        **transpile_args: Additional arguments to be passed to the transpile function.

    Attributes:
        path (str): The directory path containing the QASM files.
        category (str): The category of circuits in the directory.
        num_qubits_list (int or list, optional): The number of qubits to filter the circuits by. Defaults to None.
        _circ_dir_path (str): The full path to the directory containing the QASM files.
        _circ_name_list (list): A list of the names of the circuits in the directory.
        _curr_idx (int): The current index when iterating over the circuits.
        _remove_final_measurements (bool): Whether or not to remove the final measurements from each circuit.
        do_transpile (bool): Whether or not to transpile each circuit.
        transpile_args (dict): Additional arguments to be passed to the transpile function.

    Methods:
        __next__(): Returns the next circuit in the benchmark.
        __len__(): Returns the number of circuits in the benchmark.
        __getitem__(i): Returns the circuit at index i in the benchmark.
        get(circ_name): Returns the circuit with the given name.
        num_qubits(circ_name): Returns the number of qubits in the circuit with the given name.
        num_gates(circ_name, instruction=None): Returns the number of gates (or the number of gates of a specific type) in the circuit with the given name.
    """


    def __init__(self, path, category, num_qubits_list = None, remove_final_measurements = False, do_transpile = False, **transpile_args):
        self.path = path
        self.category = category
        self.num_qubits_list = num_qubits_list
        self._circ_dir_path = os.path.join(path, category)

        # process self._circ_name_list first
        # circuit, __get__, etc. iterate self._circ_name_list
        self._circ_name_list = next(os.walk(self._circ_dir_path))[1]
        self._process_circ_name_list()

        self._curr_idx = 0
        self._remove_final_measurements = remove_final_measurements

        self.do_transpile = do_transpile
        self.transpile_args = transpile_args


    def _order_circ_name_by_num_qubits(self):
        """
        Orders the circuits in the benchmark by the number of qubits in each circuit.
        """
        self._circ_name_list = sorted(self._circ_name_list, key=self.num_qubits)


    def _filter_num_qubit(self):
        """
        Filters the circuit names in self._circ_name_list by the number of qubits in the circuit.
        """
        processed_circ_name_list = []
        if isinstance(self.num_qubits_list, int):
            for circ_name in self._circ_name_list:
                circ_num_qubits = self.num_qubits(circ_name)
                if circ_num_qubits == self.num_qubits_list:
                    processed_circ_name_list.append(circ_name)
        elif isinstance(self.num_qubits_list, list):
            for circ_name in self._circ_name_list:
                circ_num_qubits = self.num_qubits(circ_name)
                if circ_num_qubits in self.num_qubits_list:
                    processed_circ_name_list.append(circ_name)
        elif self.num_qubits_list == None:
            processed_circ_name_list = self._circ_name_list
        
        self._circ_name_list = processed_circ_name_list


    def _process_circ_name_list(self):
        """
        Processes the list of circuit names by ordering and filtering them.
        """
        self._order_circ_name_by_num_qubits()
        self._filter_num_qubit()


    def __next__(self):
        """
        Gets the next circuit in the benchmark.

        Returns:
            The next circuit in the benchmark.

        Raises:
            StopIteration: If there are no more circuits in the benchmark.
        """
        if self._curr_idx < len(self._circ_name_list):
            self._curr_idx += 1
            return self[self._curr_idx - 1]
        else:
            raise StopIteration


    def __len__(self):
        """
        Gets the number of circuits in the benchmark.

        Returns:
            The number of circuits in the benchmark.
        """
        return len(list(self._circ_name_list))


    def __getitem__(self, i):
        """
        Gets the circuit or circuits specified by the index or slice.

        Args:
            i (int, tuple, list, or slice): The index or slice to use.

        Returns:
            The circuit or circuits specified by the index or slice.

        Raises:
            TypeError: If an invalid argument type is passed to the method.
        """
        if isinstance(i, int):
            circ_name = self._circ_name_list[i]
            return self.get(circ_name)
        elif isinstance(i, tuple):
            return [self[ii] for ii in i]
        elif isinstance(i, list):
            return [self[ii] for ii in i]
        elif isinstance(i, slice):
            return [self[ii] for ii in range(i.start if i.start else 0, min(i.stop, len(self)) if i.stop else len(self), i.step if i.step else 1)]
        else:
            raise TypeError


    @property
    def circ_list(self):
        """
        Gets the list of circuits in the benchmark.

        Returns:
            The list of circuits in the benchmark.
        """
        return self[:]


    @property
    def circ_name_list(self):
        """
        Gets the list of circuit names in the benchmark.

        Returns:
            The list of circuit names in the benchmark.
        """
        return self._circ_name_list


    def get(self, circ_name):
        """
        Returns the QuantumCircuit object corresponding to the given circuit name.

        Args:
            circ_name (str or list): The name of the circuit or a list of circuit names.

        Returns:
            A QuantumCircuit object or a list of QuantumCircuit objects.

        Raises:
            ValueError: If the circuit does not exist in the benchmark.
            TypeError: If the given circuit name is not a string or a list.
        """
        if isinstance(circ_name, str):
            if circ_name in self._circ_name_list:
                filename = os.path.join(self._circ_dir_path, circ_name, circ_name + ".qasm")
                circ = QuantumCircuit.from_qasm_file(filename)
                return self._process_circ(circ)
            else:
                raise ValueError("Circuit does not exist in the benchmark")
        elif isinstance(circ_name, list):
            return [self.get(c_name) for c_name in circ_name]
        else:
            raise TypeError


    def _process_circ(self, circ):
        """
        Processes the given QuantumCircuit object by transpiling and removing final measurements.

        Args:
            circ (QuantumCircuit): The QuantumCircuit object to be processed.

        Returns:
            The processed QuantumCircuit object.
        """
        if self.do_transpile:
            circ = transpile(circ, **self.transpile_args)
        if self._remove_final_measurements:
            circ.remove_final_measurements()
        return circ


    def num_qubits(self, circ_name):
        """
        Returns the number of qubits in the circuit with the given circuit name.

        Args:
            circ_name (str): The name of the circuit.

        Returns:
            The number of qubits in the circuit.
        """
        return int(circ_name.split("_")[-1][1:])


    def num_gates(self, circ_name, instruction = None):
        """
        Returns the number of gates in the circuit with the given instruction name.

        Args:
            circ_name (str or int): The name or index of the circuit.
            instruction (str or list[str]): The name of the instruction(s) to count (default: None).

        Returns:
            The number of gates in the circuit.

        Raises:
            IndexError: If the given index is out of range.
            TypeError: If the given circuit name is not a string or an integer.
        """
        if isinstance(circ_name, str):
            circ = self.get(circ_name)
        elif isinstance(circ_name, int):
            circ = self[circ_name]
        
        if not instruction:
            return circ.size()
        elif isinstance(instruction, str):
            return circ.size(filter_function=lambda x: x.operation.name == instruction)
        elif isinstance(instruction, list) and isinstance(instruction[0], str):
            return sum([circ.size(filter_function=lambda x: x.operation.name == ins) for ins in instruction])


    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            A string representation of the object.
        """
        return str(self)


    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            A string representation of the object.
        """
        repr_str = "Index\tCircuit Name\t\tQubits\tGates\tCX\n"
        for i, circ_name in enumerate(self._circ_name_list):
            repr_str += f"{i}\t{circ_name:<24}{self.num_qubits(circ_name)}\t{self.num_gates(circ_name)}\t{self.num_gates(circ_name, instruction='cx')}\n"
        return repr_str
