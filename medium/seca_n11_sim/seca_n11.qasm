OPENQASM 2.0;
include "qelib1.inc";
qreg q[11];
creg c[11];

z q[0];
h q[0]; // secret unitary: hz

barrier q; // Shor's error correction algorithm
cx q[0], q[3];
cx q[0], q[6];
cz q[0], q[3];
cz q[0], q[6];
h q[0];
h q[3];
h q[6];
z q[0];
z q[3];
z q[6];
cx q[0], q[1];
cx q[0], q[2];
cx q[3], q[4];
cx q[3], q[5];
cx q[6], q[7];
cx q[6], q[8];
cz q[0], q[1];
cz q[0], q[2];
cz q[3], q[4];
cz q[3], q[5];
cz q[6], q[7];
cz q[6], q[8];

// Alice starts with qubit 9.
// Bob starts with qubit 10.
// Alice is given qubit 0.
// Bob is given error-correcting qubits 1-8.
// Alice and Bob do not know what has been done to qubit 0.

barrier q; // Alice and Bob entangle their starting qubits.
h q[9];
cx q[9], q[10];

// Alice keeps qubits 0 and 9.
// Bob leaves with qubits 1-8 and 10.

barrier q; // Alice teleports the quantum state of qubit 0 to Bob's qubit.
cx q[0], q[9];
measure q[9] -> c[9];
h q[0];
cx q[9], q[10];
measure q[0] -> c[0];
cz q[0], q[10];

barrier q; // Bob corrects for bit flips and sign flips
cx q[10], q[1];
cx q[10], q[2];
cx q[3], q[4];
cx q[3], q[5];
cx q[6], q[7];
cx q[6], q[8];
cz q[10], q[1];
cz q[10], q[2];
cz q[3], q[4];
cz q[3], q[5];
cz q[6], q[7];
cz q[6], q[8];
ccx q[1], q[2], q[10];
ccx q[5], q[4], q[3];
ccx q[8], q[7], q[6];
barrier q; // start CCZ gates
h q[10];
ccx q[1], q[2], q[10];
h q[10];
h q[3];
ccx q[5], q[4], q[3];
h q[3];
h q[6];
ccx q[8], q[7], q[6];
h q[6];
barrier q; // end CCZ gates
h q[10];
h q[3];
h q[6];
z q[10];
z q[3];
z q[6];
cx q[10], q[3];
cx q[10], q[6];
cz q[10], q[3];
cz q[10], q[6];
ccx q[3], q[6], q[10];
h q[10];
ccx q[3], q[6], q[10];
h q[10];

barrier q; // Based on Alice's measurements, Bob reverses the secret unitary.
// 00 do nothing
// 01 apply X
// 10 apply Z
// 11 apply ZX
h q[10];
z q[10];
measure q[10] -> c[10];
