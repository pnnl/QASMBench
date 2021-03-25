# QASMBench Benchmark Suite

An OpenQASM benchmark suite for NISQ evaluation. The .qasm code can be directly loaded in [IBM Quantum Experience](https://quantum-computing.ibm.com/) for execution. Please see our paper ([attached](qasmbench.pdf) and [arXiv](https://arxiv.org/abs/2005.13018)) for details.

![alt text](example.png)

## Current version

Latest version: **1.2**

## About QASMBench

In this repository you will find a light-weighted benchmark suite based on IBM [OpenQASM](https://github.com/Qiskit/openqasm) language (see [spec](https://arxiv.org/pdf/1707.03429.pdf)). It collects commonly seen quantum algorithms and routines from various domains including chemistry, simulation, linear algebra, searching, optimization, arithmetic, machine learning, fault tolerance, cryptography, etc. QASMBench trades-off between generality and usability, covering the number of qubits ranging from 2 to 60K, and the circuit depth from 4 to 12M. We set most of the benchmarks with qubits less than 16 so they can be directly verified on IBM's public-available quantum machine -- [IBM Quantum Experience](https://quantum-computing.ibm.com/). You may also want to use our Density-Matrix quantum simulator ([DM-Sim](https://github.com/pnnl/DM-Sim)) that can efficiently run on CPU and GPU-clusters. 


### OpenQASM

OpenQASM (Open Quantum Assembly Language) is a low-level quantum intermediate representation (IR) for quantum instructions, similar to the traditional *Hardware-Description-Language* (HDL) like Verilog and VHDL. OpenQASM is the open-source unified low-level assembly language for IBM quantum machines publically available on cloud that have been investigated and verified by many existing research works. Several popular quantum software frameworks use OpenQASM as one of their output-formats, including [Qiskit](https://github.com/Qiskit/qiskit), [Cirq](https://github.com/quantumlib/cirq), [Scaffold](https://github.com/epiqc/ScaffCC), [ProjectQ](https://github.com/ProjectQ-Framework/ProjectQ), etc.

#### Qiskit
The *Quantum Information Software Kit* ([Qiskit](https://github.com/Qiskit/qiskit)) is a quantum software developed by *IBM*. It is based on Python. OpenQASM can be generated from Qiskit via:
```text
QuantumCircuit.qasm()
```

#### Cirq
[Cirq](https://github.com/quantumlib/cirq) is a quantum software framework from *Google*. OpenQASM can be generated from Cirq (not fully compatible) via:
```text
cirq.Circuit.to_qasm()
```

#### Scaffold
[Scaffold](https://github.com/epiqc/ScaffCC) is a quantum programming language embedded in the C/C++ programming language based on the [LLVM](https://github.com/llvm/llvm-project) compiler toolchain. A Scaffold program can be compiled by [Scaffcc](https://arxiv.org/pdf/1507.01902.pdf) to OpenQASM via "**-b**" compiler option.

#### ProjectQ
[ProjectQ](https://github.com/ProjectQ-Framework/ProjectQ) is a quantum software platform developed by *Steiger et al.* from ETH Zurich. The official website is [here](https://projectq.ch/). ProjectQ can generate OpenQASM when using IBM quantum machines as the backends:
```text
IBMBackend.get_qasm()
```

## QASMBench Benchmarks
Depending on the number of qubits used, QASMBench includes three categories. For the introduction of the benchmarking routines under each category, please see our paper for detail. For each benchmark in the following tables, we list its name, brief description, and the algorithm category it belongs to, which is based on this Nature [paper](https://www.nature.com/articles/npjqi201523) by adding the categories of quantum arithmetic, quantum machine learning and quantum communication.

The 'Gates' here refers to the number of *Standard OpenQASM gates* (see our [paper]((qasmbench.pdf))) but excluding those gates in a branching **if** statement. It is known that physical qubits in an NISQ device follow a certain topology. Since the 2-qubit gates such as **CNOT** or **CX** can only be performed between two adjacent physical qubits, a series of SWAP operations can be required to move the relevant qubits until they become directly-connected. This is an important issue in machine-specific mapping and optimization, implying a significant potential overhead. Consequently, we also list the number of CNOT gates in the tables.


### Small-scale
Qunatum circuits using **2 to 5** qubits.

| Benchmark | Description | Algorithm | Qubits | Gates | CNOT | Reference |
| :-------: |  ---------  | :-------: | :----: | :---: | :---:| :-------: |
| wstate    |  W-state preparation and assessment | Logical Operation |  3 |  30 | 9 |[OpenQASM](https://github.com/Qiskit/openqasm)|
| adder     | Quantum ripple-carry adder | Quantum Arithmetic | 4 | 23 | 10 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| basis_change | Transform the single-particle baseis of an linearly connected electronic structure | Quantum Simulation | 3 | 53 | 10 | [OpenFermion](https://github.com/quantumlib/OpenFermion-Cirq)|
| basis_trotter | Implement Trotter steps for molecule LiH at equilibrium geometry | Quantum Simulation | 4 | 1626 | 582 | [OpenFermion](https://github.com/quantumlib/OpenFermion-Cirq)|
| cat_state | Coherent superposition of two coherent states with opposite phase | Logical Operation | 4 | 4 | 3 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| deutsch | Deutsch algorithm with 2 qubits for f(x) = x | Hidden Subgroup | 2 | 5 | 1 |[OpenQASM](https://github.com/Qiskit/openqasm)|
| error_correctiond3 | Error correction with distance 3 and 5 qubits | Error Correction | 5 | 114 | 49 |[Ref](https://www.sciencedirect.com/science/article/pii/S0010465517301935)|
| fredkin | Controlled-swap gate | Logical Operation | 3 | 19 | 8 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| grover | Grover’s algorithm | Search and Optimization | 2 | 16 | 2 | [AgentANAKIN](https://github.com/AgentANAKIN/Grover-s-Algorithm)|
| hs4 | Hidden subgroup problem | Hidden Subgroup | 4 | 28 | 4 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| inverseqft | Performs an exact inversion of quantum Fourier tranform | Hidden Subgroup | 4 | 8 | 0 | [OpenQASM](https://github.com/Qiskit/openqasm)|
| ipea | Iterative phase estimation algorithm | Hidden Subgroup | 2 | 68 | 30 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| iswap | An entangling swapping gate | Logical Operation | 2 | 9 | 2 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| linearsolver | Solver for a linear equation of one qubit | Linear Equation | 3 | 19 | 4 |[Ref](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.72.032301) |
| lpn | Learning parity with noise | Machine Learning | 5 | 11 | 2 | [sampaio96](https://github.com/sampaio96/Quantum-Computing)|
| pea | Phase estimation algorithm | Hidden Subgroup | 5 | 98 | 42 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| qec_sm | Repetition code syndrome measurement | Error Correction | 5 | 5 | 4 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| qft | Quantum Fourier transform | Hidden Subgroupe | 4 | 36 | 12 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| qec_en | Quantum repetition code encoder | Error Correction | 5 | 25 | 10 | [sampaio96](https://github.com/sampaio96/Quantum-Computing)|
| teleportation | Quantum teleportation | Quantum Communication | 3 | 8 | 2 | [Ref](https://arxiv.org/abs/1607.02398)|
| toffoli | Toffoli gate | Logical Operation | 3 | 18 | 6 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| variational | Variational ansatz for a Jellium Hamiltonian with a linear-swap network | Quantum Simulation | 4 | 54 | 16 | [OpenFermion](https://github.com/quantumlib/OpenFermion-Cirq)| 
| vqe_uccsd | Variational quantum eigensolver with UCCSD | Linear Equation | 4 | 220 | 88 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| shor | Shor’s algorithm | Hidden Subgroup | 5 | 64 | 30 | [Qiskit](https://github.com/Qiskit/qiskit) |
| bell | Circuit equivalent to Bell inequality test | Logic Operation | 4 | 33 | 7 | [Cirq](https://github.com/quantumlib/cirq) |
| qrng | Quantum random number generator | Quantum Arithmetic | 4 | 4 | 0 | [Paper](https://arxiv.org/abs/1906.04410), [Repo](https://github.com/kentarotamura612/QRNG-benchmarking) |
| qaoa | Quantum approximate optimization algorithm | Search and Optimization | 3 | 15 | 6 | [Repo](https://github.com/jtiosue/QAOAPython) |
| quantumwalks | Quantum walks on graphs with up to 4 nodes | Quantum Walk | 2 | 11 | 3 | [Repo](https://github.com/raffmiceli/Quantum_Walks) |
| dnn | 3 layer quantum neural network sample | Machine Learning | 2 | 226 | 42 | [Ref](https://arxiv.org/abs/2012.00256) |


### Medium-scale
Quantum circutis using **6 to 15** qubits.


| Benchmark | Description | Algorithm | Qubits | Gates | CNOT | Reference |
| :-------: |  ---------  | :-------: | :----: | :---: | :---:| :-------: |
| adder | Quantum ripple-carry adder | Quantum Arithmetic | 10 | 142 | 65 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| bv | Bernstein-Vazirani algorithm | Hidden Subgroup | 14 | 41 | 13 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| cc | Counterfeit coin finding problem | Search and Optimization | 12 | 22 | 11 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| ising | Ising model simulation via QC | Quantum Simulation | 10 | 480 | 90 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| multiply | Performing 3×5 in a quantum circuit | Quantum Arithmetic | 13 | 98 | 40 | [AgentANAKIN](https://github.com/AgentANAKIN/Quantum-Multiplication) |
| qf21 | Using quantum phase estimation to factor the number 21 | Hidden Subgroup | 15 | 311 | 115 | [AgentANAKIN](https://github.com/AgentANAKIN/Quantum-Factoring-21) |
| qft | Quantum Fourier transform | Hidden Subgroup | 15 | 540 | 210 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| qpe | Quantum phase estimation algorithm | Hidden Subgroup | 9 | 123 | 43 | [AgentANAKIN](https://github.com/AgentANAKIN/Quantum-Phase-Estimation) |
| sat | Boolean satisfiability problem | Search and Optimization | 11 | 679 | 252 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| seca | Shor's error correction algorithm for teleportation | Error Correction | 11 | 216 | 84 | [AgentANAKIN](https://github.com/AgentANAKIN/Shors-Error-Correction-Algorithm) |
| simons | Simon’s algorithm | Hidden Subgroup | 6 | 44 | 14 | [AgentANAKIN](https://github.com/AgentANAKIN/Simon-s-Algorithm) |
| vqe_uccsd | Variational quantum eigensolver with UCCSD | Linear Equation | 6 | 2282 | 1052 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| vqe_uccsd | Variational quantum eigensolver with UCCSD | Linear Equation | 8 | 10808 | 5488 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| qaoa | Quantum approximate optimization algorithm | Search and Optimization | 6 | 270 | 54 | [Cirq](https://github.com/quantumlib/cirq) |
| bb84 | A quantum key distribution circuit | Quantum Communication | 8 | 27 | 0 | [Cirq](https://github.com/quantumlib/cirq) |
| multiplier | Quantum multiplier | Quantum Arithmetic | 15 | 574 | 246 | [Cirq](https://github.com/quantumlib/cirq) |
| dnn | 16-dimension quantum neural network sample | Machine Learning | 8 | 1008 | 192 | [Ref](https://arxiv.org/abs/2012.00256) |



### Large-scale
Quantum circuits using more than **15** qubits.

| Benchmark | Description | Algorithm | Qubits | Gates | CNOT | Reference |
| :-------: |  ---------  | :-------: | :----: | :---: | :---:| :-------: |
| dnn | quantum neural network sample | Machine Learning | 16 | 2016 | 384 | [Ref](https://arxiv.org/abs/2012.00256) |
| bigadder | Quantum ripple-carry adder | Quantum Arithmetic | 18 | 284 | 130 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| cc | Counterfeit coin finding problem via QC | Hidden Subgroup | 18 | 34 | 17 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| bv | Bernstein-Vazirani algorithm | Hidden Subgroup | 19 | 56 | 18 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| qft | Quantum Fourier tranform | Hidden Subgroup | 20 | 970 | 380 | [OpenQASM](https://github.com/Qiskit/openqasm) |
| bwt | Binary Welded Tree: a quantum walk algorithm in continuous time domain | Quantum Walk | 21 | 462001 | 174800 | QASMBench |
| cat_state | Coherent superposition of two coherent states with opposite phase | Logical Operation | 22 | 22 | 21 | QASMBench |
| ghz_state | Greenberger-Horne-Zeilinger (GHZ) state for max entanglement | Logical Operation | 23 | 23 | 22 | QASMBench |
| ising | Ising model simulation via QC | Quantum Simulation | 26 | 280 | 50 | QASMBench |
| multiplier | Quantum multiplier | Quantum Arithmetic | 25 | 1743 | 750 | [Cirq](https://github.com/quantumlib/cirq) |
| square_root | Computing the square root of an number via amplitude amplification | Quantum Arithmetic | 18 | 2300 | 898 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| swap_test | Swap test to measure quantum state distance | Machine Learning | 25 | 230 | 96 | QASMBench |
| vqe | Variational quantum eigensolver with UCCSD | Quantum Simulation | 24 | 2306072 | 1538240 | QASMBench |
| ising | Ising model simulation via QC | Quantum Simulation | 500 | 5494 | 998 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| ising | Ising model simulation via QC | Quantum Simulation | 1000 | 10994 | 1998 | [Scaffold](https://github.com/epiqc/ScaffCC) |
| class_number | Compute the class group of a real quadratic number field | Hidden Subgroups | 60052 | 31110504 | 12460637 | [Scaffold](https://github.com/epiqc/ScaffCC) |

### qelib1.inc
OpenQASM header file that defines all the gates. Please see [OpenQASM](https://github.com/Qiskit/openqasm) and our [paper](qasmbench.pdf) for details.


## QASMBenchmark Suite Structure
Each benchmark folder include the following file:
- bench.qasm: OpenQASM source file.
- bench.png: Visualization of the circuit from IBM QE.
- res_bench.png: Running results from IBM QE quantum backends (mainly 5-qubit Burlington, 15-qubit Melbourne, and 27-qubit Paris).
- bench.cuh: Source file for our [DM-Sim](https://github.com/pnnl/DM-Sim) quantum simulator.

## Tests

The small-scale benchmarks (except basis-trotter) can be directly uploaded and verified on real Quantum Machines [IBM Quantum Experience](https://quantum-computing.ibm.com/).

The medium-scale benchmarks can be either validated by real quantum machines or simulators in [IBM Quantum Experience](https://quantum-computing.ibm.com/).

Some of the large-scale benchmarks can be validated on IBM simulators. 

## DM-Sim simulation

You may also want to use our density-matrix quantum circuit simulator [DM-Sim](https://github.com/pnnl/DM-Sim) for simulating the QASMBench benchmark circuits efficiently on modern CPU (Intel X86, AMD X86, IBM Power), GPU (NVIDIA GPU and AMD GPU) and Xeon-Phi workstations or clusters ORNL Summit, ANL Theta, and NERSC Cori Supercomputers. 

## Authors 

#### [Ang Li](http://www.angliphd.com/), Pacific Northwest National Laboratory (PNNL)

#### [Sriram Krishnamoorthy](https://hpc.pnl.gov/people/sriram/), Pacific Northwest National Laboratory (PNNL)

And also the original authors that developed these quantum routines. 


## Citation format

For research articles, please cite our paper:

- Ang Li, Sriram Krishnamoorthy, "QASMBench: A Low-level QASM Benchmark Suite for NISQ Evaluation and Simulation" [[arXiv:2005.13018]](https://arxiv.org/abs/2005.13018).

Bibtex:
```text
@article{li2020qasmbench,
    title={QASMBench: A Low-level QASM Benchmark Suite for NISQ Evaluation and Simulation},
    author={Li, Ang and Krishnamoorthy, Sriram},
    journal={arXiv preprint arXiv:2005.13018},
    year={2020}
}

```


## License

This project is licensed under the BSD License, see [LICENSE](LICENSE) file for details.

## Acknowledgments

We thank the many developers and open-source community for providing these awesome quantum circuits online so we are able to collect and form this benchmark suite. This work was originally supported by PNNL's *Quantum Algorithms, Software, and Architectures* (QUASAR) LDRD Initiative. It is now supported by U.S. DOE *Co-design Center for Quantum Advantage* ([C2QA](https://www.bnl.gov/quantumcenter/)) Quantum Information Science (QIS) center XCITe crosscut. The Pacific Northwest National Laboratory (PNNL) is operated by Battelle for the U.S. Department of Energy (DOE) under contract DE-AC05-76RL01830. 

## Contributing

Please contact us If you'd like to add your circuits into the benchmark suite or you'd like to remove your circuits from the suite.
