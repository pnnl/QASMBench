#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: ipea_3*pi/8 v2
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
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	H(0);
	H(0);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	H(0);
	H(0);
	cu(dm_real, dm_imag, 0, 1);
	cu(dm_real, dm_imag, 0, 1);
	H(0);
	H(0);
	cu(dm_real, dm_imag, 0, 1);
	H(0);
}
#endif
