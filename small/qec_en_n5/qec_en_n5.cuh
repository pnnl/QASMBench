#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: Encoder into bit-flip code with parity checks (qubits 0,1,3) v2
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(2);
	T(2);
	H(2);
	H(0);
	H(1);
	H(2);
	CX(1, 2);
	CX(0, 2);
	H(0);
	H(1);
	H(3);
	CX(3, 2);
	H(2);
	H(3);
	CX(3, 2);
	CX(0, 2);
	CX(1, 2);
	H(2);
	H(4);
	CX(4, 2);
	H(2);
	H(4);
	CX(4, 2);
	CX(1, 2);
	CX(3, 2);
}
#endif
