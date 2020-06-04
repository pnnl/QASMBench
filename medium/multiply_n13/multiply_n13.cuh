#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// This initializes 13 quantum registers and 4 classical registers.
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	X(1);
	X(2);
	X(4);
// All qubits start at a ground state of 0; this changes 4 of the first 5 qubits to 1 so that I could use a binary 11 (digital 3) and a binary 101 (digital 5).
	CCX(2, 0, 5);
	CCX(2, 1, 6);
	CCX(3, 0, 7);
	CCX(3, 1, 8);
	CCX(4, 0, 9);
	CCX(4, 1, 10);
// Multiplication is all AND gates: 1 x 1 = 1; all else is 0.
	CX(6, 11);
	CX(7, 11);
	CX(8, 12);
	CX(9, 12);
// With 3 x 5, all addition can be done with simple XOR gates.
// This measures the appropriate qubits and sends the output to the classical registers for display as a histogram.
}
#endif
