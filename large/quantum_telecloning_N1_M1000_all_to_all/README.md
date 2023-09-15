# Quantum Telecloning N1 -> M1000

Performs a variant of (approximate) quantum cloning, known as quantum telecloning, copying a single qubit to 1000 approximate clones. Uses mid-circuit measurement and classical feedforward control instructions. 

- `qubit_indices_Quantum_Telecloning_N1_M1000_LNN.json` is a python-dictionary, saved as a JSON file, which contains what the qubit indices are, specifically what the message qubit is that is cloned, what the port qubit is, what the M-1 ancilla qubits are, and what the M clone qubits are. 
- Note that the clone qubits states are not measured in these circuits. In principle, if you want to characterize the clone quality, you could perform single qubit state tomography on all of the clone qubits.
- For these circuits, the pure quantum state that is cloned is parameterized by a $Ry_{pi/2}$ gate followed by a $Rz_{pi/2}$ gate. This angle could be changed and the clone quality would be unaffected because the cloning circuit is universal and symmetric.
- These circuits were exported as OpenQASM3 strings
- Compiled and optimized for an all-to-all connectivity graph
- The qasm3 file is very large, so it is compressed to save space

### Los Alamos National Laboratory Copyright Notice
© 2022. Triad National Security, LLC. All rights reserved. This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S. Department of Energy/National Nuclear Security Administration. All rights in the program are reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear Security Administration. The Government is granted for itself and others acting on its behalf a nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare derivative works, distribute copies to the public, perform publicly and display publicly, and to permit others to do so.

LANL C Number: C22038

### License
This program is open source under the BSD-3 License. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
