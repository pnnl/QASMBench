// Name of Experiment: Encoder into bit-flip code with parity checks (qubits 0,1,3) v2

OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[5];

h q[2];
t q[2];
h q[2];
h q[0];
h q[1];
h q[2];
cx q[1], q[2];
cx q[0], q[2];
h q[0];
h q[1];
h q[3];
cx q[3], q[2];
h q[2];
h q[3];
cx q[3], q[2];
cx q[0], q[2];
cx q[1], q[2];
h q[2];
h q[4];
cx q[4], q[2];
h q[2];
h q[4];
cx q[4], q[2];
cx q[1], q[2];
cx q[3], q[2];


measure q[2] -> c[2];
measure q[4] -> c[4];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[3] -> c[3];
