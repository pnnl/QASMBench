#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

//@author Raymond Harry Rudy rudyhar@jp.ibm.com
//Counterfeit coin finding with 11 coins.
//The false coin is 6
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
	CX(0, 11);
	CX(1, 11);
	CX(2, 11);
	CX(3, 11);
	CX(4, 11);
	CX(5, 11);
	CX(6, 11);
	CX(7, 11);
	CX(8, 11);
	CX(9, 11);
	CX(10, 11);
}
#endif
