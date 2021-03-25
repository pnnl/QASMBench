// Generated from Cirq v0.8.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
qreg q[15];
creg m_result[3];


x q[13];
x q[12];
x q[10];
x q[9];

// Gate: <__main__.Multiplier object at 0x7f0de092ec40>
ccx q[12],q[9],q[1];
ccx q[12],q[10],q[4];
ccx q[12],q[11],q[7];
ccx q[1],q[2],q[3];
cx q[1],q[2];
ccx q[0],q[2],q[3];
ccx q[4],q[5],q[6];
cx q[4],q[5];
ccx q[3],q[5],q[6];
cx q[7],q[8];
cx q[6],q[8];
ccx q[3],q[5],q[6];
cx q[4],q[5];
ccx q[4],q[5],q[6];
cx q[4],q[5];
cx q[3],q[5];
ccx q[0],q[2],q[3];
cx q[1],q[2];
ccx q[1],q[2],q[3];
cx q[1],q[2];
cx q[0],q[2];
ccx q[12],q[9],q[1];
ccx q[12],q[10],q[4];
ccx q[12],q[11],q[7];
ccx q[13],q[9],q[4];
ccx q[13],q[10],q[7];
ccx q[1],q[2],q[3];
cx q[1],q[2];
ccx q[0],q[2],q[3];
ccx q[4],q[5],q[6];
cx q[4],q[5];
ccx q[3],q[5],q[6];
cx q[7],q[8];
cx q[6],q[8];
ccx q[3],q[5],q[6];
cx q[4],q[5];
ccx q[4],q[5],q[6];
cx q[4],q[5];
cx q[3],q[5];
ccx q[0],q[2],q[3];
cx q[1],q[2];
ccx q[1],q[2],q[3];
cx q[1],q[2];
cx q[0],q[2];
ccx q[13],q[9],q[4];
ccx q[13],q[10],q[7];
ccx q[14],q[9],q[7];
ccx q[1],q[2],q[3];
cx q[1],q[2];
ccx q[0],q[2],q[3];
ccx q[4],q[5],q[6];
cx q[4],q[5];
ccx q[3],q[5],q[6];
cx q[7],q[8];
cx q[6],q[8];
ccx q[3],q[5],q[6];
cx q[4],q[5];
ccx q[4],q[5],q[6];
cx q[4],q[5];
cx q[3],q[5];
ccx q[0],q[2],q[3];
cx q[1],q[2];
ccx q[1],q[2],q[3];
cx q[1],q[2];
cx q[0],q[2];
ccx q[14],q[9],q[7];

measure q[2] -> m_result[0];
measure q[5] -> m_result[1];
measure q[8] -> m_result[2];
