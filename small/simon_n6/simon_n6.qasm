OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg c[6];
// This initializes 6 quantum registers and 6 classical registers.

h q[0];
h q[1];
h q[2];
// The first 3 qubits are put into superposition states.

barrier q;
cx q[2], q[4];
x q[3];
cx q[2], q[3];
ccx q[0], q[1], q[3];
x q[0];
x q[1];
ccx q[0], q[1], q[3];
x q[0];
x q[1];
x q[3];
// This applies the secret structure: s=110.

barrier q;
h q[0];
h q[1];
h q[2];

// This measures the first 3 qubits.
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];

// This measures the second 3 qubits.
measure q[3] -> c[3];
measure q[4] -> c[4];
measure q[5] -> c[5];
