#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: pea_3*pi/8 v3
__device__ __inline__ void cu1fixed(double* dm_real, double* dm_imag, const unsigned c, const unsigned t)
{
	U1(-1.1780972451, t);
	CX(c, t);
	U1(1.1780972451, t);
	CX(c, t);
}
__device__ __inline__ void cu(double* dm_real, double* dm_imag, const unsigned c, const unsigned t)
{
	cu1fixed(dm_real, dm_imag, c, t);
}
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	H(3);
	cu(dm_real, dm_imag, 3, 4);
	cu(dm_real, dm_imag, 2, 4);
	cu(dm_real, dm_imag, 2, 4);
	cu(dm_real, dm_imag, 1, 4);
	cu(dm_real, dm_imag, 1, 4);
	cu(dm_real, dm_imag, 1, 4);
	cu(dm_real, dm_imag, 1, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	cu(dm_real, dm_imag, 0, 4);
	H(0);
	CU1(-1.57079632679, 0, 1);
	H(1);
	CU1(-0.785398163397, 0, 2);
	CU1(-1.57079632679, 1, 2);
	H(2);
	CU1(-0.392699081699, 0, 3);
	CU1(-0.785398163397, 1, 3);
	CU1(-1.57079632679, 2, 3);
	H(3);
}
#endif
