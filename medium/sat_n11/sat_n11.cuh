#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Quantum code for the specified SAT problem.
// Declare all needed (qu)bits
// Prepare uniform superposition
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(1);
	H(2);
	H(3);
	H(4);
// Marking with oracle evaluation
	X(5);
	X(6);
	X(7);
	X(8);
	X(4);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 5);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(2);
	X(3);
	X(4);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 6);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(1);
	X(2);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 7);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(1);
	X(2);
	CCX(2, 3, 8);
	X(2);
	X(3);
	CCX(5, 6, 9);
	CCX(7, 9, 10);
	CCX(8, 10, 0);
	CCX(7, 9, 10);
	CCX(5, 6, 9);
	X(2);
	X(3);
	CCX(2, 3, 8);
	X(1);
	X(2);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 7);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(1);
	X(2);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 6);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(2);
	X(3);
	X(4);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 5);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	X(4);
// Amplitude amplification
	H(1);
	H(2);
	H(3);
	H(4);
	X(0);
	X(1);
	X(2);
	X(3);
	X(4);
	H(0);
	CCX(1, 2, 9);
	CCX(3, 9, 10);
	CCX(4, 10, 0);
	CCX(3, 9, 10);
	CCX(1, 2, 9);
	H(0);
	X(0);
	X(1);
	X(2);
	X(3);
	X(4);
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
// Measurements
}
#endif
