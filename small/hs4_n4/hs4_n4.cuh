#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	H(3);
	X(0);
	X(2);
	H(1);
	H(3);
	CX(0, 1);
	CX(2, 3);
	H(1);
	H(3);
	X(0);
	X(2);
	H(0);
	H(1);
	H(2);
	H(3);
	H(1);
	H(3);
	CX(0, 1);
	CX(2, 3);
	H(1);
	H(3);
	H(0);
	H(1);
	H(2);
	H(3);
}
#endif
