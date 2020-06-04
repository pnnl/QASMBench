// Generated from Cirq v0.8.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [(0, 0), (0, 1), (1, 0), (1, 1)]
qreg q[4];
creg m_b[1];
creg m_y[1];
creg m_a[1];
creg m_x[1];


h q[0];
h q[1];
h q[3];
cx q[0],q[2];
rx(pi*-0.25) q[0];

// Gate: CNOT**0.5
ry(pi*-0.5) q[2];
u3(pi*0.5,0,pi*0.75) q[3];
u3(pi*0.5,0,pi*0.25) q[2];
rx(pi*0.5) q[3];
cx q[3],q[2];
rx(pi*0.25) q[3];
ry(pi*0.5) q[2];
cx q[2],q[3];
rx(pi*-0.5) q[2];
rz(pi*0.5) q[2];
cx q[3],q[2];
u3(pi*0.5,pi*0.5,pi*1.0) q[3];
u3(pi*0.5,pi*1.0,pi*1.0) q[2];
ry(pi*0.5) q[2];

// Gate: CNOT**0.5
ry(pi*-0.5) q[0];
u3(pi*0.5,0,pi*0.75) q[1];
u3(pi*0.5,0,pi*0.25) q[0];
rx(pi*0.5) q[1];
cx q[1],q[0];
rx(pi*0.25) q[1];
ry(pi*0.5) q[0];
cx q[0],q[1];
rx(pi*-0.5) q[0];
rz(pi*0.5) q[0];
cx q[1],q[0];
u3(pi*0.5,pi*0.5,pi*1.0) q[1];
u3(pi*0.5,pi*1.0,pi*1.0) q[0];
ry(pi*0.5) q[0];

measure q[2] -> m_b[0];
measure q[3] -> m_y[0];
measure q[0] -> m_a[0];
measure q[1] -> m_x[0];
