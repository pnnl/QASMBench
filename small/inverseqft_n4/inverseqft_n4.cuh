#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// QFT and measure, version 2
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	H(3);
	H(0);
	H(1);
	H(2);
	H(3);
}
#endif
