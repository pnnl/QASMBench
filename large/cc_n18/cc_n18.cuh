#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

//@author Raymond Harry Rudy rudyhar@jp.ibm.com
//Counterfeit coin finding with 17 coins.
//The false coin is 12
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
	CX(0, 17);
	CX(1, 17);
	CX(2, 17);
	CX(3, 17);
	CX(4, 17);
	CX(5, 17);
	CX(6, 17);
	CX(7, 17);
	CX(8, 17);
	CX(9, 17);
	CX(10, 17);
	CX(11, 17);
	CX(12, 17);
	CX(13, 17);
	CX(14, 17);
	CX(15, 17);
	CX(16, 17);
}
#endif
