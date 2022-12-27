import os
from qiskit import QuantumCircuit

def verify_circuit(qasm_path):
    QuantumCircuit.from_qasm_file(qasm_path)

def verify_cat(cat):
    cat_circ = next(os.walk('../'+cat+'/'))[1]
    for circ in cat_circ:
        path = str("../" + cat + '/' + circ + '/' + circ + ".qasm")
        print ('checking ' + path + '...\n')
        verify_circuit(path)

verify_cat('small')
#verify_cat('medium')
#verify_cat('large')
