#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Generated from Cirq v0.8.0
// Qubits: [0, 1, 2, 3, 4, 5, 6, 7]
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	H(1);
	X(2);
	X(3);
	X(4);
	X(5);
	H(7);
	H(5);
	H(1);
	H(2);
	H(4);
	H(7);
	X(0);
	H(1);
	X(2);
	X(3);
	X(4);
	H(7);
	H(5);
	H(6);
	H(2);
	H(4);
	H(1);
	H(3);
	H(7);
	H(2);
	H(4);
}
#endif
