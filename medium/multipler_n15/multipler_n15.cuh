#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Generated from Cirq v0.8.0
// Qubits: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(13);
	X(12);
	X(10);
	X(9);
// Gate: <__main__.Multiplier object at 0x7f0de092ec40>
	CCX(12, 9, 1);
	CCX(12, 10, 4);
	CCX(12, 11, 7);
	CCX(1, 2, 3);
	CX(1, 2);
	CCX(0, 2, 3);
	CCX(4, 5, 6);
	CX(4, 5);
	CCX(3, 5, 6);
	CX(7, 8);
	CX(6, 8);
	CCX(3, 5, 6);
	CX(4, 5);
	CCX(4, 5, 6);
	CX(4, 5);
	CX(3, 5);
	CCX(0, 2, 3);
	CX(1, 2);
	CCX(1, 2, 3);
	CX(1, 2);
	CX(0, 2);
	CCX(12, 9, 1);
	CCX(12, 10, 4);
	CCX(12, 11, 7);
	CCX(13, 9, 4);
	CCX(13, 10, 7);
	CCX(1, 2, 3);
	CX(1, 2);
	CCX(0, 2, 3);
	CCX(4, 5, 6);
	CX(4, 5);
	CCX(3, 5, 6);
	CX(7, 8);
	CX(6, 8);
	CCX(3, 5, 6);
	CX(4, 5);
	CCX(4, 5, 6);
	CX(4, 5);
	CX(3, 5);
	CCX(0, 2, 3);
	CX(1, 2);
	CCX(1, 2, 3);
	CX(1, 2);
	CX(0, 2);
	CCX(13, 9, 4);
	CCX(13, 10, 7);
	CCX(14, 9, 7);
	CCX(1, 2, 3);
	CX(1, 2);
	CCX(0, 2, 3);
	CCX(4, 5, 6);
	CX(4, 5);
	CCX(3, 5, 6);
	CX(7, 8);
	CX(6, 8);
	CCX(3, 5, 6);
	CX(4, 5);
	CCX(4, 5, 6);
	CX(4, 5);
	CX(3, 5);
	CCX(0, 2, 3);
	CX(1, 2);
	CCX(1, 2, 3);
	CX(1, 2);
	CX(0, 2);
	CCX(14, 9, 7);
}
#endif
