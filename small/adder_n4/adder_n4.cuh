#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	X(1);
	H(3);
	CX(2, 3);
	T(0);
	T(1);
	T(2);
	TDG(3);
	CX(0, 1);
	CX(2, 3);
	CX(3, 0);
	CX(1, 2);
	CX(0, 1);
	CX(2, 3);
	TDG(0);
	TDG(1);
	TDG(2);
	T(3);
	CX(0, 1);
	CX(2, 3);
	S(3);
	CX(3, 0);
	H(3);
}
#endif
