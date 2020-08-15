// Finding the max of the cost function: C = -1 + z(0)z(2) - 2 z(0)z(1)z(2) - 3 z(1) 
// Starting with p = 1
// Generated from Cirq v0.8.0

OPENQASM 2.0;
include "qelib1.inc";

// Qubits: [(0, 0), (1, 0), (2, 0)]
qreg q[3];
creg m2[1];
creg m0[1];
creg m1[1];

h q[0];
h q[1];
h q[2];
cx q[0],q[2];
rz(pi*1.79986) q[2];
cx q[0],q[2];
cx q[0],q[1];
cx q[1],q[2];
rz(pi*-3.59973) q[2];
cx q[1],q[2];
cx q[0],q[1];
rx(pi*0.545344) q[2];
rz(pi*-5.39959) q[1];
rx(pi*0.545344) q[0];
measure q[2] -> m2[0];
rx(pi*0.545344) q[1];
measure q[0] -> m0[0];
measure q[1] -> m1[0];

