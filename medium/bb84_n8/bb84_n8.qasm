// Generated from Cirq v0.8.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [0, 1, 2, 3, 4, 5, 6, 7]
qreg q[8];

creg m6[1];
creg m0[1];
creg m3[1];
creg m1[1];
creg m2[1];
creg m4[1];
creg m5[1];
creg m7[1];


x q[0];
h q[1];
x q[2];
x q[3];
x q[4];
x q[5];
h q[7];
measure q[6] -> m6[0];
h q[5];
h q[1];
h q[2];
h q[4];
h q[7];
measure q[0] -> m0[0];
measure q[3] -> m3[0];
measure q[1] -> m1[0];
measure q[2] -> m2[0];
measure q[4] -> m4[0];
measure q[5] -> m5[0];
measure q[7] -> m7[0];
x q[0];
h q[1];
x q[2];
x q[3];
x q[4];
h q[7];
h q[5];
h q[6];
h q[2];
h q[4];
h q[1];
h q[3];
h q[7];
measure q[0] -> m0[0];
measure q[5] -> m5[0];
measure q[6] -> m6[0];
h q[2];
h q[4];
measure q[1] -> m1[0];
measure q[3] -> m3[0];
measure q[7] -> m7[0];
measure q[2] -> m2[0];
measure q[4] -> m4[0];
