OPENQASM 2.0;
include "qelib1.inc";
qreg bits[4];
creg c[4];

h bits[0];
cx bits[0],bits[1];
cx bits[1],bits[2];
cx bits[2],bits[3];

measure bits[0] -> c[0];
measure bits[1] -> c[1];
measure bits[2] -> c[2];
measure bits[3] -> c[3];
