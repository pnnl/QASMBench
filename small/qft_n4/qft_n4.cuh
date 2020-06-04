#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// quantum Fourier transform
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(0);
	X(2);
	H(0);
	CU1(1.57079632679, 1, 0);
	H(1);
	CU1(0.785398163397, 2, 0);
	CU1(1.57079632679, 2, 1);
	H(2);
	CU1(0.392699081699, 3, 0);
	CU1(0.785398163397, 3, 1);
	CU1(1.57079632679, 3, 2);
	H(3);
}
#endif
