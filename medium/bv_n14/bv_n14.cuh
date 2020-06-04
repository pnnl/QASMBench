#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

//@author Raymond Harry Rudy rudyhar@jp.ibm.com
//Bernstein-Vazirani with 14 qubits.
//Hidden string is 1111111111111
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
	H(5);
	H(6);
	H(7);
	H(8);
	H(9);
	H(10);
	H(11);
	H(12);
	X(13);
	H(13);
	CX(0, 13);
	CX(1, 13);
	CX(2, 13);
	CX(3, 13);
	CX(4, 13);
	CX(5, 13);
	CX(6, 13);
	CX(7, 13);
	CX(8, 13);
	CX(9, 13);
	CX(10, 13);
	CX(11, 13);
	CX(12, 13);
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
	H(5);
	H(6);
	H(7);
	H(8);
	H(9);
	H(10);
	H(11);
	H(12);
}
#endif
