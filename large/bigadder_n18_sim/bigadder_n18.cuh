#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// quantum ripple-carry adder
// 8-bit adder made out of 2 4-bit adders from adder.qasm
// Cuccaro et al, quant-ph/0410184
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
// add a to b, storing result in b
__device__ __inline__ void add4(double* dm_real, double* dm_imag, const unsigned a0, const unsigned a1, const unsigned a2, const unsigned a3, const unsigned b0, const unsigned b1, const unsigned b2, const unsigned b3, const unsigned cin, const unsigned cout)
{
	majority(dm_real, dm_imag, cin, b0, a0);
	majority(dm_real, dm_imag, a0, b1, a1);
	majority(dm_real, dm_imag, a1, b2, a2);
	majority(dm_real, dm_imag, a2, b3, a3);
	CX(a3, cout);
	unmaj(dm_real, dm_imag, a2, b3, a3);
	unmaj(dm_real, dm_imag, a1, b2, a2);
	unmaj(dm_real, dm_imag, a0, b1, a1);
	unmaj(dm_real, dm_imag, cin, b0, a0);
}
// add two 8-bit numbers by calling the 4-bit ripple-carry adder
// carry bit on output lives in carry[0]
// set input states
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	X(2);
	X(10);
	X(11);
	X(12);
	X(13);
	X(14);
	X(15);
	X(16);
	X(17);
	X(16);
// output should be 11000000 0
	add4(dm_real, dm_imag, 2, 3, 4, 5, 10, 11, 12, 13, 0, 1);
	add4(dm_real, dm_imag, 6, 7, 8, 9, 14, 15, 16, 17, 1, 0);
}
#endif
