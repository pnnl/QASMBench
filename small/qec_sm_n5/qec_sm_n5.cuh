#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Repetition code syndrome measurement
__device__ __inline__ void syndrome(double* dm_real, double* dm_imag, const unsigned d1, const unsigned d2, const unsigned d3, const unsigned a1, const unsigned a2)
{
	CX(d1, a1);
	CX(d2, a1);
	CX(d2, a2);
	CX(d3, a2);
}
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	syndrome(dm_real, dm_imag, 0, 1, 2, 3, 4);
}
#endif
