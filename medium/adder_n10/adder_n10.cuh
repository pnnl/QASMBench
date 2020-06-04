#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// quantum ripple-carry adder from Cuccaro et al, quant-ph/0410184
__device__ __inline__ void majority(double* dm_real, double* dm_imag, const unsigned a, const unsigned b, const unsigned c)
{
	CX(c, b);
	CX(c, a);
	CCX(a, b, c);
}
__device__ __inline__ void unmaj(double* dm_real, double* dm_imag, const unsigned a, const unsigned b, const unsigned c)
{
	CCX(a, b, c);
	CX(c, a);
	CX(a, b);
}
// set input states
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(1);
	X(5);
	X(6);
	X(7);
	X(8);
// add a to b, storing result in b
	majority(dm_real, dm_imag, 0, 5, 1);
	majority(dm_real, dm_imag, 1, 6, 2);
	majority(dm_real, dm_imag, 2, 7, 3);
	majority(dm_real, dm_imag, 3, 8, 4);
	CX(4, 9);
	unmaj(dm_real, dm_imag, 3, 8, 4);
	unmaj(dm_real, dm_imag, 2, 7, 3);
	unmaj(dm_real, dm_imag, 1, 6, 2);
	unmaj(dm_real, dm_imag, 0, 5, 1);
}
#endif
