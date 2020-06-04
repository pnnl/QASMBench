#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

// Name of Experiment: lineair_solver_in_0 v3
// Description: 1bit lineair solver
// Solver for a linear equation for one quantumbit
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	X(2);
	CX(0, 1);
	H(0);
	H(1);
	H(2);
	CX(2, 1);
	H(1);
	H(2);
	U3(-0.58, 0, 0, 2);
	H(1);
	H(2);
	CX(2, 1);
	H(1);
	H(2);
	H(0);
	U3(0.58, 0, 0, 2);
	CX(0, 1);
	H(0);
}
#endif
