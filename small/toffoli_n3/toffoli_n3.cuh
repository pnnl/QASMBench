#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	X(1);
	H(2);
	CX(1, 2);
	TDG(2);
	CX(0, 2);
	T(2);
	CX(1, 2);
	TDG(2);
	CX(0, 2);
	TDG(1);
	T(2);
	CX(0, 1);
	H(2);
	TDG(1);
	CX(0, 1);
	T(0);
	S(1);
}
#endif
