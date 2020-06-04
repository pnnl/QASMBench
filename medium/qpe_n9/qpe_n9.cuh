#ifndef CIRCUIT_CUH
#define CIRCUIT_CUH

//This initializes 9 quantum and 6 classical registers.
// initialize ancilla qubits
__device__ __inline__ void circuit(double* dm_real, double* dm_imag)
{
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
	H(5);
// eigenstates of the unitary operator
	X(6);
	X(7);
	X(8);
//I extended the pattern formed by the 3-qubit and 6-qubit implementations.
	CCX(5, 6, 7);
	CZ(7, 8);
	CCX(5, 6, 7);
//This 4-qubit controlled-Z gate is from this webpage.
	CU1(-0.0981747704247, 5, 0);
	CU1(-0.196349540849, 5, 1);
	CU1(-0.392699081699, 5, 2);
	CU1(-0.785398163397, 5, 3);
	CU1(-1.57079632679, 5, 4);
	CU1(-0.196349540849, 4, 0);
	CU1(-0.392699081699, 4, 1);
	CU1(-0.785398163397, 4, 2);
	CU1(-1.57079632679, 4, 3);
	CU1(-0.392699081699, 3, 0);
	CU1(-0.785398163397, 3, 1);
	CU1(-1.57079632679, 3, 2);
	CU1(-0.785398163397, 2, 0);
	CU1(-1.57079632679, 2, 1);
	CU1(-1.57079632679, 1, 0);
//This would obviously be more efficient using Python FOR loops, but you can copy-and-paste that from IBM Q Experience and there’s no fun in that. If I eventually implement this in Shor’s algorithm, I’ll use Python.
	H(0);
	H(1);
	H(2);
	H(3);
	H(4);
	H(5);
}
#endif
