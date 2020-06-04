#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

//@author Raymond Harry Rudy rudyhar@jp.ibm.com
//Bernstein-Vazirani with 19 qubits.
//Hidden string is 111111111111111111
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
	H(13);
	H(14);
	H(15);
	H(16);
	H(17);
	X(18);
	H(18);
	CX(0, 18);
	CX(1, 18);
	CX(2, 18);
	CX(3, 18);
	CX(4, 18);
	CX(5, 18);
	CX(6, 18);
	CX(7, 18);
	CX(8, 18);
	CX(9, 18);
	CX(10, 18);
	CX(11, 18);
	CX(12, 18);
	CX(13, 18);
	CX(14, 18);
	CX(15, 18);
	CX(16, 18);
	CX(17, 18);
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
	H(13);
	H(14);
	H(15);
	H(16);
	H(17);
}
#endif
