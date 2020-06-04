// Generated from Cirq v0.8.0
OPENQASM 2.0;
include "qelib1.inc";

// Qubits: [0, 1, 2, 3]
qreg q[4];
creg c[4];

z q[0];
z q[1];
z q[2];
z q[3];

// Gate: PhasedISWAP**-1.0
rz(pi*0.25) q[1];
rz(pi*-0.25) q[2];
cx q[1],q[2];
h q[1];
cx q[2],q[1];
rz(pi*-0.5) q[1];
cx q[2],q[1];
rz(pi*0.5) q[1];
h q[1];
cx q[1],q[2];
rz(pi*-0.25) q[1];
rz(pi*0.25) q[2];

// Gate: PhasedISWAP**0.08130614625631793
rz(pi*0.25) q[0];
rz(pi*-0.25) q[1];
cx q[0],q[1];
h q[0];
cx q[1],q[0];
rz(pi*0.0406530731) q[0];
cx q[1],q[0];
rz(pi*-0.0406530731) q[0];
h q[0];
cx q[0],q[1];
rz(pi*-0.25) q[0];
rz(pi*0.25) q[1];

// Gate: PhasedISWAP**-0.08130614625631793
rz(pi*0.25) q[2];
rz(pi*-0.25) q[3];
cx q[2],q[3];
h q[2];
cx q[3],q[2];
rz(pi*-0.0406530731) q[2];
cx q[3],q[2];
rz(pi*0.0406530731) q[2];
h q[2];
cx q[2],q[3];
rz(pi*-0.25) q[2];
rz(pi*0.25) q[3];

rz(pi*0.1123177385) q[0];

// Gate: PhasedISWAP**-1.0
rz(pi*0.25) q[1];
rz(pi*-0.25) q[2];
cx q[1],q[2];
h q[1];
cx q[2],q[1];
rz(pi*-0.5) q[1];
cx q[2],q[1];
rz(pi*0.5) q[1];
h q[1];
cx q[1],q[2];
rz(pi*-0.25) q[1];
rz(pi*0.25) q[2];

rz(pi*0.1123177385) q[1];
rz(pi*0.0564909955) q[3];
rz(pi*0.0564909955) q[2];

// Gate: PhasedISWAP**-1.0
rz(pi*0.25) q[1];
rz(pi*-0.25) q[2];
cx q[1],q[2];
h q[1];
cx q[2],q[1];
rz(pi*-0.5) q[1];
cx q[2],q[1];
rz(pi*0.5) q[1];
h q[1];
cx q[1],q[2];
rz(pi*-0.25) q[1];
rz(pi*0.25) q[2];

// Gate: PhasedISWAP**-0.05102950815299322
rz(pi*0.25) q[0];
rz(pi*-0.25) q[1];
cx q[0],q[1];
h q[0];
cx q[1],q[0];
rz(pi*-0.0255147541) q[0];
cx q[1],q[0];
rz(pi*0.0255147541) q[0];
h q[0];
cx q[0],q[1];
rz(pi*-0.25) q[0];
rz(pi*0.25) q[1];

// Gate: PhasedISWAP**0.05102950815299322
rz(pi*0.25) q[2];
rz(pi*-0.25) q[3];
cx q[2],q[3];
h q[2];
cx q[3],q[2];
rz(pi*0.0255147541) q[2];
cx q[3],q[2];
rz(pi*-0.0255147541) q[2];
h q[2];
cx q[2],q[3];
rz(pi*-0.25) q[2];
rz(pi*0.25) q[3];

swap q[3],q[2];
swap q[1],q[0];
swap q[2],q[1];
swap q[3],q[2];
swap q[1],q[0];
swap q[2],q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];

