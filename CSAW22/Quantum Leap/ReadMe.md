# Quantum Leap writeup
![Categorie](https://img.shields.io/badge/Category-Misc-blue?style=for-the-badge)

## Description
> My friend took the quantum leap and purchased a quantum computer with two qubits. They mentioned using a quantum logic gate to input the flag and they gave me the computers output. I have been stuck and Can NOT figure out the flag.
> 
> The file [output.txt](./output.txt) was attached to the description

## Exploit
The description mentions that we're dealing with a quantum computer with two qubits, se we can assume that the gate the person used to get the output is a two-qubit quantum logic gate.

A quantum gate is basic quantum circuit operating on a small number of qubits, they perform operations to change the state of the qubits, and unlike many classical logic gates, quantum logic gates are reversible.
Each quantum gate has its matrix, and since the qubit states are represented with vectors, the gates transform these vectors to get new states.
The state vectors of the states |0> and |1> are:

![2022-09-15_19h32_37](https://user-images.githubusercontent.com/68945305/190504993-8094b514-dfa2-472f-8622-59867ef2e061.png)


The CNOT gate was applied, it's a two-qubit quantum gate that performs a controlled NOT where one qubit is the control and the second qubit is the target.
Its matrix is the following :

![2022-09-15_19h33_11](https://user-images.githubusercontent.com/68945305/190486028-970479de-3ff1-415e-bdd2-b4f0e6c8dab2.png)

When applied:

![2022-09-15_20h47_02](https://user-images.githubusercontent.com/68945305/190497970-bd14060b-e413-43b6-982a-17da2d1c18a5.png)

The mathematics behind these results are simple: 

Lets take |10> and |11>:

![2022-09-15_21h46_45](https://user-images.githubusercontent.com/68945305/190505635-f998a0df-a328-4230-a3f1-1e3be73a5cef.png)

This ⊗ represents a tensor product, you can read about it here if you don't know what it is : https://www.math3ma.com/blog/the-tensor-product-demystified

The first qubit is usually referred to as the control qubit and the second qubit as the target qubit. Expressed in basis states, the CNOT gate:
leaves the control qubit unchanged and performs a Pauli-X gate or NOT gate (which just flips the state of the qubit) on the target qubit when the control qubit is in state ∣1⟩;
leaves the target qubit unchanged when the control qubit is in state ∣0⟩.

As you may have noticed, this challenge can be done manually by converting the output string to binary, taking two bits at a time and checking the value of the most significant bit, if it's 1, the other bit is flipped, else, nothing is done.

I wanted to solve this task with the CNOT gate itself,using the qiskit module in python.
Qiskit is an open-source SDK for working with quantum computers at the level of pulses, circuits, and application modules.

As mentioned before quantum logic gates are reversible, in this case, when CNOT gate is applied once on the output, we get the flag.

Here's the script, you can run it on jupyter notebook: 
```
from qiskit import *

output = 'wxqvn$Zae${deyZv$d"i'
output_array = ''.join(format(i, '08b') for i in bytearray(output, encoding ='utf-8'))

bin_flag = ''

def state_vect(bit):
    if(bit == '0'):
        vect = [1, 0]
    else : 
        vect = [0 ,1]
    return vect

i = 0
while i<len(output_array):
    
    #Initialize the quantum circuit
    q = QuantumRegister(2, "q")
    c = ClassicalRegister(2, "c")
    
    qc = QuantumCircuit(q,c)

    #get the initial state from the output
    vect0 = state_vect(output_array[i])
    vect1 = state_vect(output_array[i+1])
    
    #initialize the register
    qc.initialize(vect1,0)
    qc.initialize(vect0,1)
    
    qc.measure(q, c)

    #apply the CNOT gate, q[1] is the control and q[0] is the target
    qc.cx(q[1],q[0])

    qc.measure(q, c)
    
    #execute the circuit
    qobj = assemble(qc, shots=1)
    job = execute(qc,Aer.get_backend('qasm_simulator'),shots=1)
    counts = job.result().get_counts()
    
    bin_flag += str(counts)[2:4]
    
    #Increment the counter to get the next 2 qubits
    i=i+2
    
flag = ''.join(chr(int(bin_flag[i*8:i*8+8],2)) for i in range(len(bin_flag)//8))
print(flag)
```
flag{4_qu4ntum_g4t3}
