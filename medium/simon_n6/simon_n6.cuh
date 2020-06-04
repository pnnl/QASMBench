#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// This initializes 6 quantum registers and 6 classical registers.
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
// The first 3 qubits are put into superposition states.
	CX(2, 4);
	X(3);
	CX(2, 3);
	CCX(0, 1, 3);
	X(0);
	X(1);
	CCX(0, 1, 3);
	X(0);
	X(1);
	X(3);
// This applies the secret structure: s=110.
	H(0);
	H(1);
	H(2);
// This measures the first 3 qubits.
// This measures the second 3 qubits.
}
#endif
