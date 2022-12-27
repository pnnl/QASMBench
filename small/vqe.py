import numpy as np
from qiskit.aqua.algorithms import VQE, NumPyEigensolver
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import qiskit
import sys
import random

# Generating a random hamiltonian : https://arxiv.org/abs/1907.09530

try:
    k = int(sys.argv[1])
except:
    print("Run from CLI for interactive K,defaulting K = 3")
    k = 3

with open("../../SUPPORTED_GATES",'r') as file:
    VALID_GATES = eval(file.read())



class VQE():
    def __init__(self,k):
        self.PAULI_MATRICES = {'Z':np.array([[1, 0], [0, -1]]),
                               'X':np.array([[0,1],[1,0]]),
                               'Y':np.array([[0,0-1j],[0+1j,0]]),
                               'I': np.array([[1,0],[0,1]])}
        self.k = k
        self.circuit = None
        self.hamiltonian = np.zeros((2**k,2**k))
        self.generate_random_hamiltonian_matrix()
        self.generate_trainable_circuit()

    def generate_random_hamiltonian_matrix(self):
        print(self.PAULI_MATRICES)
        weights = np.random.randint(10, size=10)
        for weight in weights:
            new_matrix = 1
            for i in range(k):
                new_matrix = np.kron(new_matrix, self.PAULI_MATRICES[self.z_or_i()])
            self.hamiltonian += new_matrix*weight*0.5

    def z_or_i(self):
        p=0.5
        if random.random() > p:
            return "Z"
        else:
            return "I"

    def generate_trainable_circuit(self):
        self.circuit = qiskit.circuit.library.EfficientSU2(num_qubits=k,entanglement='linear')
        self.circuit = qiskit.compiler.transpile(self.circuit,basis_gates=['cx','rz','sx','id','x'])
        n_param = self.circuit.num_parameters
        self.circuit = self.circuit.assign_parameters(np.random.rand(n_param)*np.pi)
        self.circuit.measure_all()

        print(self.circuit)


if __name__=='__main__':
    np.random.seed(42)
    vqe = VQE(k)
    vqe.generate_random_hamiltonian_matrix()
    if not os.path.isdir("qasm"):
        os.mkdir("qasm")
    qasm_file = open(f"qasm/vqe_n{k}.qasm", "w")
    qasm_file.write(vqe.circuit.qasm())
    qasm_file.close()
