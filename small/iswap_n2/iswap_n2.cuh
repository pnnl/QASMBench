#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: iswap v4
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	S(0);
	S(1);
	H(0);
	CX(0, 1);
	H(0);
	H(1);
	CX(0, 1);
	H(0);
}
#endif
