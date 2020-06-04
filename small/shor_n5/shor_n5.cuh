#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	H(4);
	H(4);
	H(4);
	CX(4, 2);
	CX(4, 0);
	H(4);
	H(4);
	CSWAP(4, 1, 0);
	CSWAP(4, 2, 1);
	CSWAP(4, 3, 2);
	CX(4, 3);
	CX(4, 2);
	CX(4, 1);
	CX(4, 0);
	H(4);
}
#endif
