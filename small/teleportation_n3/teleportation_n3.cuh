#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Teleportation using 3 qubits.
// Description: Based on the example given by S. Fedortchenko (https://arxiv.org/pdf/1607.02398.pdf)
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	T(0);
	H(0);
	H(2);
	S(0);
	CX(2, 1);
	CX(0, 1);
	H(0);
}
#endif
