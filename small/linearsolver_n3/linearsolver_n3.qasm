// Name of Experiment: lineair_solver_in_0 v3
// Description: 1bit lineair solver
// Solver for a linear equation for one quantumbit

OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

h q[0];
x q[2];
cx q[0],q[1];
h q[0];
h q[1];
h q[2];
cx q[2],q[1];
h q[1];
h q[2];
u3(-0.58,0,0) q[2];
h q[1];
h q[2];
cx q[2],q[1];
h q[1];
h q[2];
h q[0];
u3(0.58,0,0) q[2];
cx q[0],q[1];
h q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
