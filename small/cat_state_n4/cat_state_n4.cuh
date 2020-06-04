#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	CX(0, 1);
	CX(1, 2);
	CX(2, 3);
}
#endif
