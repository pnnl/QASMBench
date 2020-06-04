OPENQASM 2.0;
include "qelib1.inc";
qreg q[15];
creg c[10];

// initialize ancilla qubits
h q[0];
h q[1];
h q[2];
h q[3];
h q[4];
h q[5];
h q[6];
h q[7];
h q[8];
h q[9];
// eigenstate of the unitary operator: 21 (10101)
x q[10];
x q[12];
x q[14];

barrier q; // unitary operator
ccx q[9], q[10], q[12];
ccx q[11], q[12], q[13];
cz q[13], q[14];
ccx q[11], q[12], q[13];
ccx q[9], q[10], q[12];

barrier q; // inverse Quantum Fourier Transform (QFT)
cu1(-pi/512) q[9], q[0];
cu1(-pi/256) q[9], q[1];
cu1(-pi/128) q[9], q[2];
cu1(-pi/64) q[9], q[3];
cu1(-pi/32) q[9], q[4];
cu1(-pi/16) q[9], q[5];
cu1(-pi/8) q[9], q[6];
cu1(-pi/4) q[9], q[7];
cu1(-pi/2) q[9], q[8];

cu1(-pi/256) q[8], q[0];
cu1(-pi/128) q[8], q[1];
cu1(-pi/64) q[8], q[2];
cu1(-pi/32) q[8], q[3];
cu1(-pi/16) q[8], q[4];
cu1(-pi/8) q[8], q[5];
cu1(-pi/4) q[8], q[6];
cu1(-pi/2) q[8], q[7];

cu1(-pi/128) q[7], q[0];
cu1(-pi/64) q[7], q[1];
cu1(-pi/32) q[7], q[2];
cu1(-pi/16) q[7], q[3];
cu1(-pi/8) q[7], q[4];
cu1(-pi/4) q[7], q[5];
cu1(-pi/2) q[7], q[6];

cu1(-pi/64) q[6], q[0];
cu1(-pi/32) q[6], q[1];
cu1(-pi/16) q[6], q[2];
cu1(-pi/8) q[6], q[3];
cu1(-pi/4) q[6], q[4];
cu1(-pi/2) q[6], q[5];

cu1(-pi/32) q[5], q[0];
cu1(-pi/16) q[5], q[1];
cu1(-pi/8) q[5], q[2];
cu1(-pi/4) q[5], q[3];
cu1(-pi/2) q[5], q[4];

cu1(-pi/16) q[4], q[0];
cu1(-pi/8) q[4], q[1];
cu1(-pi/4) q[4], q[2];
cu1(-pi/2) q[4], q[3];

cu1(-pi/8) q[3], q[0];
cu1(-pi/4) q[3], q[1];
cu1(-pi/2) q[3], q[2];

cu1(-pi/4) q[2], q[0];
cu1(-pi/2) q[2], q[1];

cu1(-pi/2) q[1], q[0];

barrier q; // output should be 6 (binary 110)
h q[0];
//measure q[0] -> c[0];
h q[1];
//measure q[1] -> c[1];
h q[2];
//measure q[2] -> c[2];
h q[3];
//measure q[3] -> c[3];
h q[4];
//measure q[4] -> c[4];
h q[5];
//measure q[5] -> c[5];
h q[6];
//measure q[6] -> c[6];
h q[7];
measure q[7] -> c[7];
h q[8];
measure q[8] -> c[8];
h q[9];
measure q[9] -> c[9];
