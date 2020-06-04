#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	Z(0);
	H(0);
	CX(0, 3);
	CX(0, 6);
	CZ(0, 3);
	CZ(0, 6);
	H(0);
	H(3);
	H(6);
	Z(0);
	Z(3);
	Z(6);
	CX(0, 1);
	CX(0, 2);
	CX(3, 4);
	CX(3, 5);
	CX(6, 7);
	CX(6, 8);
	CZ(0, 1);
	CZ(0, 2);
	CZ(3, 4);
	CZ(3, 5);
	CZ(6, 7);
	CZ(6, 8);
// Alice starts with qubit 9.
// Bob starts with qubit 10.
// Alice is given qubit 0.
// Bob is given error-correcting qubits 1-8.
// Alice and Bob do not know what has been done to qubit 0.
	H(9);
	CX(9, 10);
// Alice keeps qubits 0 and 9.
// Bob leaves with qubits 1-8 and 10.
	CX(0, 9);
	H(0);
	CX(9, 10);
	CZ(0, 10);
	CX(10, 1);
	CX(10, 2);
	CX(3, 4);
	CX(3, 5);
	CX(6, 7);
	CX(6, 8);
	CZ(10, 1);
	CZ(10, 2);
	CZ(3, 4);
	CZ(3, 5);
	CZ(6, 7);
	CZ(6, 8);
	CCX(1, 2, 10);
	CCX(5, 4, 3);
	CCX(8, 7, 6);
	H(10);
	CCX(1, 2, 10);
	H(10);
	H(3);
	CCX(5, 4, 3);
	H(3);
	H(6);
	CCX(8, 7, 6);
	H(6);
	H(10);
	H(3);
	H(6);
	Z(10);
	Z(3);
	Z(6);
	CX(10, 3);
	CX(10, 6);
	CZ(10, 3);
	CZ(10, 6);
	CCX(3, 6, 10);
	H(10);
	CCX(3, 6, 10);
	H(10);
// 00 do nothing
// 01 apply X
// 10 apply Z
// 11 apply ZX
	H(10);
	Z(10);
}
#endif
