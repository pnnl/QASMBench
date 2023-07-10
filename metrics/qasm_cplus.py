# ---------------------------------------------------------------------------
# SV-Sim: Density-Matrix Quantum Circuit Simulation Environement
# ---------------------------------------------------------------------------
# Ang Li, Senior Computer Scientist
# Pacific Northwest National Laboratory(PNNL), U.S.
# Homepage: http://www.angliphd.com
# GitHub repo: http://www.github.com/pnnl/SV-Sim
# PNNL-IPID: 31919-E, ECCN: EAR99, IR: PNNL-SA-143160
# BSD Lincese.
# ---------------------------------------------------------------------------
# File: svsim_qasm_cplus.py
# Translate OpenQASM assembly code to SVSim C++ code
# ---------------------------------------------------------------------------

import argparse
import string
import os
import cmath
import sys
import math

#======= Description ========
# Try to address two types of circuits in OpenQASM code:
# (1) User-defined functional module circuit 
# (2) Main circuits 

#=======  Global tables and variables =========

# Starndard gates are gates defined in OpenQASM header.
# Dictionary in {"gate name": number of standard gates inside}
STANDARD_GATE_TABLE = {
        "u3":1,  #3-parameter 2-pulse single qubit gate
        "u2":1,  #2-parameter 1-pulse single qubit gate
        "u1":1,  #1-parameter 0-pulse single qubit gate
        "cx":1,  #controlled-NOT
        "id":1,  #idle gate(identity)
        "x":1,   #Pauli gate: bit-flip
        "y":1,   #Pauli gate: bit and phase flip
        "z":1,   #Pauli gate: phase flip
        "h":1,   #Clifford gate: Hadamard
        "s":1,   #Clifford gate: sqrt(Z) phase gate
        "sdg":1, #Clifford gate: conjugate of sqrt(Z)
        "t":1,   #C3 gate: sqrt(S) phase gate
        "tdg":1, #C3 gate: conjugate of sqrt(S)
        "rx":1,  #Rotation around X-axis
        "ry":1,  #Rotation around Y-axis
        "rz":1,  #Rotation around Z-axis
        "c1":1,  #Arbitrary 1-qubit gate
        "c2":1,  #Arbitrary 2-qubit gate
        "sx":1  #Square root of X-gate
        }  

# Composition gates are gates defined in OpenQASM header.
# Dictionary in {"gate name": number of standard gates inside}
COMPOSITION_GATE_TABLE = {
        "cz":3,       #Controlled-Phase
        "cy":3,       #Controlled-Y
        "swap":3,     #Swap
        "ch":11,      #Controlled-H
        "ccx":15,     #C3 gate: Toffoli
        "cswap":17,   #Fredkin
        "crx":5,      #Controlled RX rotation
        "cry":4,      #Controlled RY rotation
        "crz":4,      #Controlled RZ rotation
        "cu1":5,      #Controlled phase rotation
        "cu3":5,      #Controlled-U
        "rxx":7,      #Two-qubit XX rotation
        "rzz":3,      #Two-qubit ZZ rotation
        "rccx":9,     #Relative-phase CCX
        "rc3x":18,    #Relative-phase 3-controlled X gate
        "c3x":27,     #3-controlled X gate
        "c3sqrtx":27, #3-controlled sqrt(X) gate
        "c4x":87,     #4-controlled X gate
        "cp":5,  # Controlled phase
        "cu":7,  # Controlled U gate
        }

# OpenQASM native gate table, other gates are user-defined.
GATE_TABLE = dict(STANDARD_GATE_TABLE)
GATE_TABLE.update(COMPOSITION_GATE_TABLE)


# ==================================================================================
# For the statistics of the number of CNOT or CX gate in the circuit

# Number of CX in Standard gates
STANDARD_CX_TABLE = { "u3":0, "u2":0, "u1":0, "cx":1, "id":0, "x":0, "y":0, "z":0, "h":0, 
                     "s":0, "sdg":0, "t":0, "tdg":0, "rx":0, "ry":0, "rz":0, "c1":0, "c2":1, "sx":0} 
# Number of CX in Composition gates
COMPOSITION_CX_TABLE = {"cz":1, "cy":1, "swap":3, "ch":2, "ccx":6, "cswap":8, "crx":2, "cry":2,
        "crz":2, "cu1":2, "cu3":2, "rxx":2, "rzz":2, "rccx":3, "rc3x":6, "c3x":6, "c3sqrtx":6,
        "c4x":18, "cu":2, "cp":2}
CX_TABLE = dict(STANDARD_CX_TABLE)
CX_TABLE.update(COMPOSITION_CX_TABLE)

# We need to map from a user-defined local qubit-register to a unified global array for SV-Sim
global_array = {}  #Field start position
field_length = {}  #Field length
gate_num = 0
cx_num = 0
seg_num = 0
SM = "sm_70"

# To register and look-up user-defined function in QASM
# Format: {"function_name": gate_num}
function_table = {}
# Format: {"function_name": cx_gate_num}
cx_table = {}

#Keywords in QASM that are currently not used
other_keys = ["measure", "barrier", "OPENQASM", "include", "creg", "if", "reset"]

#======= Helper Function ========
def get_op(line):
    if line.find("(") != -1:
        line = line[:line.find("(")].strip()
    op = line.split(" ")[0].strip()
    return op

#=======  Mapping Functions  =========
# Mapping from qreg to global array
def qreg_to_ga(qreg_string):
    #print (qreg_string)
    if qreg_string.find("[") != -1:
        field = qreg_string[:qreg_string.find("[")].strip()
        field_shift = int(qreg_string[qreg_string.find("[")+1:qreg_string.find("]")])
        ga_shift = str(global_array[field] + field_shift)
    else:
        field = qreg_string.strip()
        ga_shift = ""
        #if field.find("(") != -1:
            #expr = field[field.find("(")+1:field.find(")")]
            #for item in expr.split(","):
                #ga_shift = str(eval(item.strip(), {'pi':cmath.pi})) + ", "
            #ga_shift = ga_shift[:-2]
            #ga_shift = str(eval(expr, {'pi':cmath.pi}))
            #field = field[field.find(")")+1:].strip()
        if field in global_array:
            ga_shift += str(global_array[field])
        else:
            ga_shift += field
    return ga_shift

# Mapping for a param_list, such as "cout[3], cin[2], par[0]"
def paramlist_to_ga(param_list):
    slist = []
    recursive = False
    if param_list.find(')') != -1: 
        recursive = True
        slist.append("")
        gate_param = param_list.split(')')[0].split(',')
        gate_param = [p.strip().strip('(').strip() for p in gate_param]
        for expr in gate_param:
            slist[0] +=  str(eval(expr, {'pi':cmath.pi})) + ", "
        param_list = param_list.split(')')[1]
    params = param_list.strip(';').split(",")
    params = [i.strip() for i in params]
    #check if any param is a vector
    num_bits = 1
    for param in params:
        if (param.find('[') == -1) and (param in field_length) and field_length[param]>1:
            num_bits = field_length[param]
            break
    for b in range(0,num_bits):
        s = ""
        for param in params:
            if param != "":
                if (param.find('[') == -1) and (param in field_length) and field_length[param]>1:
                    if b >= field_length[param]:
                        print ("Error in Syntax!")
                        exit()
                    else:
                        param = param + '[' + str(b) + ']'
                ga_shift = qreg_to_ga(param)
                s += str(ga_shift) + ", "
        if recursive:
            slist[-1] = slist[-1] + s[:-2]
        else:
            slist.append(s[:-2])
    #print (slist, num_bits)
    return slist

# Look up built-in or user-defined gates in a user-defined gate function
def function_gate(line, line_id):
    s = str("")
    n = 0
    cx = 0
    line = line.strip()
    if line == "":
        return s, n, cx
    op = get_op(line)
    if op in function_table: # User-defined gate function
        s = "\t" + op + "(sim, " 
        #line = line[len(op)+1:-1].replace(')','),')
        line = line[len(op)+1:].replace(')','),')
        params = line.split(",")
        #print (params)
        for param in params:
            s += param.strip() + ", " 
        s = s[:-2] + "):\n"
        n = function_table[op]
        cx = cx_table[op]
    elif op in GATE_TABLE: # OpenQASM built-in gate
        paramlist_ga = paramlist_to_ga(line[line.find(" ")+1:])
        for p in paramlist_ga:
            s += "\tsim." + op.upper() + "(" + p + ");\n"
        n = len(paramlist_ga) * GATE_TABLE[op]
        cx = len(paramlist_ga) * CX_TABLE[op]
    elif op in ['{','}']:
        s = ""
    else:
        print ('==Line-' + str(line_id) + ': "' + line + '" is not a gate in Function!')
    return s,n,cx

# Look up built-in gates in the global circuit
def builtin_gate(line, line_id):
    s = str("")
    n = 0
    cx = 0
    line = line.strip()
    if line == "":
        return s
    op = get_op(line)
    if op in GATE_TABLE:
        if line.find("(") != -1:
            line = line.replace("("," (")
            line = line.replace(")","),")
            #print (line)
        paramlist_ga = paramlist_to_ga(line[line.find(" ")+1:])
        for p in paramlist_ga:
            s += "\tsim." + op.upper() + "(" + p + ");\n"
        n = len(paramlist_ga) * GATE_TABLE[op]
        cx = len(paramlist_ga) * CX_TABLE[op]
    else:
        print ('==Line-' + str(line_id) + ': "' + line + '" is not a gate!')
    return s, n, cx


## Parsing the source OpenQASM file line by line
def parse(infile, mainfile):
    global global_array
    global field_length
    global function_table
    global cx_table
    global gate_num
    global cx_num
    global seg_num
    prev_gate_num = 0
    qreg_idx = 0
    start_global_circuit = False
    s = str("")
    outfile = mainfile
    lines = infile.readlines()
    i = 0
    while i < len(lines):
        l = lines[i].strip().strip('\n')
        s = ""
        if l != "":
            ## User-defined comments, 
            if l.lstrip().startswith("//"):
                s += '//' + l[l.find("//")+2:] + "\n"
                outfile.write(s)
            else:
                # If comment at end, extract op
                if l.find("//") != -1:
                    l = l[:l.find("//")]
               # Start to parse
                op = get_op(l)
                # Invoke user-defined function
                if op in function_table: 
                    s = "\t"
                    paramlist_ga = paramlist_to_ga(l[len(op)+1:-1])
                    for p in paramlist_ga:
                        s += "" + op + "(sim, " + p + ")\n"
                    gate_num += len(paramlist_ga) * function_table[op]
                    cx_num += len(paramlist_ga) * cx_table[op]
                # User-defined gate function definition
                elif op == "gate":
                    ll = l.split(" ")
                    gate_name = ll[1].strip()
                    qregs = ll[2].strip().split(",")
                    params = ""
                    pos = gate_name.find('(')
                    n = 0
                    cx = 0
                    if  pos != -1: #extra params
                        gate_name = gate_name[:pos]
                        params = gate_name[pos+1:gate_name.find(')')].strip()
                    s = "void " + gate_name \
                            + "(Simulation &sim"
                    if params != "":
                        for param in params.split(','):
                            s += ", " + param
                    for qreg in qregs:
                        s += ", " + qreg
                    s += ")\n{\n" 
                    i = i+1 #jump {
                    l = lines[i].strip().strip('\n')
                    while not l.startswith("}"):
                        #print ("Parsing " + l)
                        ll = l.split(";")
                        for g in ll:
                            s1, n1, cx1 = function_gate(g,i)
                            s += s1
                            n += n1
                            cx += cx1
                        i = i+1
                        l = lines[i].strip().strip('\n')
                    s += "}\n\n"
                    function_table[gate_name] = n
                    cx_table[gate_name] = cx
                #Define quantum register, build up global array
                elif op == "qreg":
                    ll = l.split(" ")[1] 
                    field = ll[:ll.find("[")]
                    bits = int(ll[ll.find("[")+1:ll.find("]")])
                    global_array[field] = qreg_idx
                    field_length[field] = bits
                    qreg_idx += bits
                #Built-in gate invokation
                elif op in GATE_TABLE:
                    if start_global_circuit is False:
                        start_global_circuit = True
                        s = 'void prepare_circuit(Simulation &sim)\n{\n'
                    else:
                        s = ""
                    ss, n, cx = builtin_gate(l,i)
                    gate_num += n
                    s += ss 
                    cx_num += cx
                #Measure
                #elif op == "measure":
                    #ll = l.split(" ")[1] 
                    #field = ll[:ll.find("[")]
                    #bits = int(ll[ll.find("[")+1:ll.find("]")])
                    #s = "\tsim.M(" + str(bits) + ");\n"
                #Other keywords not-realized
                elif op in other_keys:
                    s = ""
                else:
                    print ("Unknown symbol: " + op)
                outfile.write(s)
        i = i+1
    s = "}\n\n"
    outfile.write(s)


# Main Program
parser = argparse.ArgumentParser(description='SV-Sim Assembler for OpenQASM-V2.0: translating OpenQASM to SV-Sim native simulation circuit code.')
parser.add_argument('--input', '-i', help='input OpenQASM file, such as adder.qasm')
parser.add_argument('--output', '-o', default='svsim_circuit.cpp', help='output SV-Sim circuit C++/CUDA file (default: svsim_circuit.cpp)') 
args = parser.parse_args()
#print (args.input)

# Parsing input and Writing to output
qasmfile = open(args.input, "r")
svfile = open(args.output, "w")

svfile.write("#include <stdio.h>\n")
svfile.write("#include <mpi.h>\n")
svfile.write('#include "../../src/util.h"\n')
svfile.write('#include "../../src/dmsim_nvgpu_mpi.cuh"\n')

svfile.write('//Use the NWQSim namespace to enable C++/CUDA APIs\n')
svfile.write('using namespace NWQSim;\n\n')

parse(qasmfile, svfile)
qasmfile.close()

maxvalidx = max(global_array, key=global_array.get)
nqubits = global_array[maxvalidx] + field_length[maxvalidx]


svfile.write('int main(int argc, char *argv[])\n{\n')
svfile.write('\tMPI_Init(&argc, &argv);\n')
svfile.write('\tSimulation sim;\n')
svfile.write('\tprepare_circuit(sim);\n')
svfile.write('\tsim.sim();\n')
svfile.write('\tMPI_Finalize();\n')
svfile.write('\treturn 0;\n}\n')
svfile.close()

print ("== SV-Sim: Translating " + args.input + " to " + args.output + " ==")
print ("Number of qubits: " + str(nqubits))
print ("Number of basic gates: " + str(gate_num))
print ("Number of cnot gates: " + str(cx_num))

#cmd = "python " + args.output + " " + str(nqubits)
#os.system(cmd)

