# SecretMessage2 writeup
![Categorie](https://img.shields.io/badge/Category-Quantum-blue?style=for-the-badge)

## Description
>
> I want to tell you a secret, but i'm afraid someone will intercept our communication. I know how good you are now with quantum encoding, so I will let you figure it out on your own. 
> I used the following code to get to encode the secret:
 ```
 qc.s(q[2])
 qc.ccx(q[0],q[1],q[2])
 qc.h(q[2])
 qc.swap(q[1],q[0])
 qc.y(q[0])
 ```
>The secret is: VMëÜÁÂÎèÜ
>
>Also, the secret contains two english words, it doesn't contain special characters nor numbers.
>
>Flag format: Securinets{decoded_message}
>
>BE CAREFUL, YOU ONLY HAVE 5 attempts
>
>Author: mida0ui

## Solution
From the description of this task, we can see that the CCNOT gate was used, along with other gates to encode the message, meaning that we need to use a quantum register containing 3 qubits to solve this task. The CCNOT gate is similar to the CNOT gate seen in the previous task, but it's a three-qubit gate, it is applied to one target qubit based on the state of two control qubits:

![2023-03-24_12h41_54](https://user-images.githubusercontent.com/68945305/227512203-39c1f52b-4c32-426e-8fb8-676bf2740cd8.png)

To encode the message, a very special gate waas used too, the Hadamard gate.
The Hadamard gate is a single-qubit operation that maps the basis state ∣0⟩ to ![2023-03-24_12h45_04](https://user-images.githubusercontent.com/68945305/227512818-c69dc67e-3b9a-4110-806a-68a1d8259f4f.png) = |+> and |1> to ![2023-03-24_12h45_39](https://user-images.githubusercontent.com/68945305/227512923-b68d7c97-22fb-4e3b-9ca3-59e835b93bf9.png) = |->, thus creating an equal superposition of the two basis states.
It has the matrix:

![2023-03-24_12h55_46](https://user-images.githubusercontent.com/68945305/227514820-95d36f4c-11ce-47bb-bdcf-ef68002436e0.png)


A qubit can exist in a superposition of its two "basis" states, which loosely means that it is in both states simultaneously. When measuring a qubit, the result is a probabilistic output of a classical bit, so for one single qubit, the measurement can give either |1> or |0> depending on the probabilistic state.
With that said, we cannot use one iteration to decode the message like in the previous task, we need to print all the possibilities (or almost) to see the different reults of measurements, and get the decoded message.
To make the task easier and less time consuming, the description specifies that the secret contains two english words and it doesn't contain special characters nor numbers. So we will filter the results based on these two facts.

```
import matplotlib
from qiskit import *
import re

output = 'VMëÜÁÂÎèÜ'
output_array = ''.join(format(i, '08b') for i in bytearray(output, encoding="windows-1252"))

bin_flag = ''
bins = ''
def state_vect(bit):
    if(bit == '0'):
        vect = [1, 0]
    else : 
        vect = [0 ,1]
    return vect

while(1):
    i = 0
    flag = ""
    while i<len(output_array):

        #Initialize the quantum circuit
        q = QuantumRegister(3, "q")
        c = ClassicalRegister(3, "c")

        qc = QuantumCircuit(q,c)

        #get the initial state from the output
        vect0 = state_vect(output_array[i])
        vect1 = state_vect(output_array[i+1])
        vect2 = state_vect(output_array[i+2])

        #in itialize the register
        qc.initialize(vect0,2)
        qc.initialize(vect1,1)
        qc.initialize(vect2,0)


        qc.measure(q, c)

        #Reverse the circuit
        qc.y(q[0])  
        qc.swap(q[1],q[0])     
        qc.h(q[2])
        qc.ccx(q[0],q[1],q[2])
        qc.s(q[2])


        qc.measure(q, c)

        #execute the circuit
        qobj = assemble(qc, shots=1)
        job = execute(qc,Aer.get_backend('qasm_simulator'),shots=1)
        counts = job.result().get_counts()

        bin_flag += str(counts)[2:5]
        #Increment the counter to get the next 2 qubits
        i=i+3

    flag = ''.join(chr(int(bin_flag[i*8:i*8+8],2)) for i in range(len(bin_flag)//8))
    if(bool(re.match('^[a-zA-Z]*$',flag))==True):
        print(flag)
    bin_flag = ''
    ```
Flag: Securinets{youwin}
