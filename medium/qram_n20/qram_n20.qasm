// Bucket brigade qRAM prototype circuit reproduced from https://iopscience.iop.org/article/10.1088/1367-2630/17/12/123010/pdf
// see the original paper or the circuit figure for details 
// 3-bit readin lines |a2 a1 a0> = 010
// 8 QRAM entries from m000 to m111
// 4-bit readout line, measures the entangled state of addr and qout

OPENQASM 2.0;
include "qelib1.inc";

qreg addr[3];
qreg rout[8];
qreg ram[8];
qreg qout[1];
creg cout[4];

//sample quantum input to addr, addr[0] is MSB (big-endian)
x addr[1];

//sample data in ram, ram = 10000101
x ram[0];
x ram[2];
x ram[7];

//initialize fixed routing
x rout[7];

// routing circuit
// 1st level routing for |a0>
cx addr[0], rout[3];
cx rout[3], rout[7];

// 2nd level routing for |a1>
ccx addr[1], rout[3], rout[1];
cx rout[1], rout[3];
ccx addr[1], rout[7], rout[5];
cx rout[5], rout[7];

// 3rd level routing for |a2>
ccx addr[2], rout[1], rout[0];
ccx addr[2], rout[3], rout[2];
ccx addr[2], rout[5], rout[4];
ccx addr[2], rout[7], rout[6];
cx rout[0], rout[1];
cx rout[2], rout[3];
cx rout[4], rout[5];
cx rout[6], rout[7];


// coupling circuit
ccx rout[7], ram[7], qout[0];
ccx rout[6], ram[6], qout[0];
ccx rout[5], ram[5], qout[0];
ccx rout[4], ram[4], qout[0];
ccx rout[3], ram[3], qout[0];
ccx rout[2], ram[2], qout[0];
ccx rout[1], ram[1], qout[0];
ccx rout[0], ram[0], qout[0];


// Deentangling circuit for 3rd level routing (|a2>)
cx rout[6], rout[7];
cx rout[4], rout[5];
cx rout[2], rout[3];
cx rout[0], rout[1];
ccx addr[2], rout[7], rout[6];
ccx addr[2], rout[5], rout[4];
ccx addr[2], rout[3], rout[2];
ccx addr[2], rout[1], rout[0];

// Deentangling circuit for 2nd level routing (|a1>)
cx rout[5], rout[7];
ccx addr[1], rout[7], rout[5];
cx rout[1], rout[3];
ccx addr[1], rout[3], rout[1];

// Deentangling circuit for 1st level routing (|a0>)
cx rout[3], rout[7];
cx addr[0], rout[3];

// measure queried data
measure addr[0] -> cout[0];
measure addr[1] -> cout[1];
measure addr[2] -> cout[2];
measure qout[0] -> cout[3];