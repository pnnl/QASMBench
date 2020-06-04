#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: W-state v1
__device__ __inline__ void cH(double* dm_real, double* dm_imag, const unsigned a, const unsigned b)
{
	H(b);
	SDG(b);
	CX(a, b);
	H(b);
	T(b);
	CX(a, b);
	T(b);
	H(b);
	S(b);
	X(b);
	S(a);
}
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	U3(1.91063, 0, 0, 0);
	cH(dm_real, dm_imag, 0, 1);
	CCX(0, 1, 2);
	X(0);
	X(1);
	CX(0, 1);
}
#endif
