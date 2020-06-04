#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: Grover N=2 A=10 v1
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(1);
	CX(0, 1);
	H(1);
	H(0);
	H(1);
	X(0);
	X(1);
	H(1);
	CX(0, 1);
	H(1);
	X(0);
	X(1);
	H(0);
	H(1);
}
#endif
