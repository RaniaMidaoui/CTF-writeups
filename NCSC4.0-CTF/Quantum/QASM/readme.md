# Quantum Leap writeup
![Categorie](https://img.shields.io/badge/Category-Quantum-blue?style=for-the-badge)

## Description: 
>Can you make this quantum circuit work? Flag Format: Securinets{output}
>
>Author: mida0ui

The file "circuit.qasm" was attached with the task, you can find it in this repo.

First of all, what is QASM?

QASM(quantum assembly language) is a simple text-format language for describing acyclic quantum circuits composed from single qubit, multiply controlled single-qubit gates, multiple-qubit, and multiple-qubit controlled multiple-qubit gates.
A QASM program declares the classical bits and qubits, describes the operations (gates) on those qubits and the measurements needed to obtain the classical result by inspecting the qubits. 

In this challenge, the only thing that needs to be done is to open the qasm file and run the circuit describes.
This can be done in various ways, there's no single intended solution, i will only state 2 solutions in this writeup. 

### Solution 1:
You can import the code in the QASM file in IBM Quantum composer: https://quantum-computing.ibm.com/composer/files/new
![2023-03-23_14h03_27](https://user-images.githubusercontent.com/68945305/227212904-65c59610-ca9d-47d8-9c10-77d5a778a901.png)

Yhe output of this circuit is always 01001 (with a 100% probability).
Flag: Securinets{01001}

### Solution 2:
You can import the QASM file code and run the circuit using qiskit.
In this case, to make the quantum circuit work, you only have to add measurements.

```
from qiskit import *

qasm_str = """OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];
y q[0];
y q[2];
x q[3];
y q[1];
id q[3];
id q[1];
z q[0];
y q[0];
ccx q[2], q[3], q[4];
swap q[0], q[1];
cx q[3], q[4];
x q[2];
x q[0];
cx q[2], q[3];
y q[0];
x q[2];
swap q[2], q[3];
cx q[3], q[4];
ccx q[0], q[1], q[2];
y q[4];
z q[3];
y q[2];
cx q[2], q[3];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
"""

circuit = QuantumCircuit.from_qasm_str(qasm_str)

backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()

print(result.get_counts(circuit))
```

The reuslt of this code is: 
![2023-03-23_15h35_19](https://user-images.githubusercontent.com/68945305/227237110-fde0799f-7c11-46f7-b979-5e875700b573.png)

But the circuit contains a quantum register of 5 qubits, we have to get the measurement result of them all: we notice that all the quantum gates described in the QASM file did not change the state of the fifth qubit, so its still in the default value.
The default state of a qubit, if not initialisaed is |0>.
So the overall output of the circuit is 01001 (always, with a 100% probability).

Flag: Securinets{01001}

