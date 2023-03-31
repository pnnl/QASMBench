# Usage

## [QASMBench interface for qiskit](./qiskit.py)

A class for managing a collection of QASM circuits for benchmarking.
The interface can behave like a iterator, a list, or a dict.


1. Initiate the object:

    ```python
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
    ```

2. Retrieve Circuits:

   1. Behave like a iterator:

        ```python
        circ_1 = next(bm)
        circ_2 = next(bm)
        ```

   2. Behave like a list:

        ```python
        circ = bm[0]
        circ_list = bm[:2]
        ```
   3. Behave like a dict:

        ```python
        circ = bm.get("teleportation_n3")
        circ_list = bm.get(["teleportation_n3", "adder_n4"])
        ```

3. Get information of the benchmark:

    ```python
    # the list of all circuits
    circ_list = bm.circ_list

    # the list of all circuit names
    circ_list = bm.circ_name_list

    # return the length of the benchmark
    bm_length = len(bm)
    ```