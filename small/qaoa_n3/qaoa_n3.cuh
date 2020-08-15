#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Finding the max of the cost function: C = -1 + z(0)z(2) - 2 z(0)z(1)z(2) - 3 z(1)
// Starting with p = 1
// Generated from Cirq v0.8.0
// Qubits: [(0, 0), (1, 0), (2, 0)]
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	CX(0, 2);
	RZ(5.65442695349, 2);
	CX(0, 2);
	CX(0, 1);
	CX(1, 2);
	RZ(-11.3088853229, 2);
	CX(1, 2);
	CX(0, 1);
	RX(1.71324870408, 2);
	RZ(-16.9633122764, 1);
	RX(1.71324870408, 0);
	RX(1.71324870408, 1);
}
#endif
