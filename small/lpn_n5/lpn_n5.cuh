#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: LPN circuit 2 v1
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(3);
	H(4);
	CX(3, 2);
	CX(0, 2);
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
}
#endif
