// Generated from Cirq v0.8.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [0, 1, 2, 3, 4, 5, 6, 7]
qreg q[8];
creg m_6[1];
creg m_0[1];
creg m_3[1];
creg m_1[1];
creg m_2[1];
creg m_4[1];
creg m_5[1];
creg m_7[1];


x q[0];
h q[1];
x q[2];
x q[3];
x q[4];
x q[5];
h q[7];
measure q[6] -> m_6[0];
h q[5];
h q[1];
h q[2];
h q[4];
h q[7];
measure q[0] -> m_0[0];
measure q[3] -> m_3[0];
measure q[1] -> m_1[0];
measure q[2] -> m_2[0];
measure q[4] -> m_4[0];
measure q[5] -> m_5[0];
measure q[7] -> m_7[0];
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
measure q[0] -> m_0[0];
measure q[5] -> m_5[0];
measure q[6] -> m_6[0];
h q[2];
h q[4];
measure q[1] -> m_1[0];
measure q[3] -> m_3[0];
measure q[7] -> m_7[0];
measure q[2] -> m_2[0];
measure q[4] -> m_4[0];
