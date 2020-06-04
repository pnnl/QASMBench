#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	X(1);
	CX(2, 1);
	CX(0, 1);
	H(2);
	T(0);
	TDG(1);
	T(2);
	CX(2, 1);
	CX(0, 2);
	T(1);
	CX(0, 1);
	TDG(2);
	TDG(1);
	CX(0, 2);
	CX(2, 1);
	T(1);
	H(2);
	CX(2, 1);
}
#endif
