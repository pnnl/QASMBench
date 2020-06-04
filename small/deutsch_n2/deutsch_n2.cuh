#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Implementation of Deutsch algorithm with two qubits for f(x)=x
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(1);
	H(0);
	H(1);
	CX(0, 1);
	H(0);
}
#endif
