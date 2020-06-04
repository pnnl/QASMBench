// Teleportation using 3 qubits.
// Description: Based on the example given by S. Fedortchenko (https://arxiv.org/pdf/1607.02398.pdf) 

OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

h q[0];
t q[0];
h q[0];
h q[2];
s q[0];
cx q[2],q[1];
cx q[0],q[1];
h q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
