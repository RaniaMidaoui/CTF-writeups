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

        #initialize the register
        qc.initialize(vect0,2)
        qc.initialize(vect1,1)
        qc.initialize(vect2,0)


        qc.measure(q, c)

        #Reverse the circuit
        qc.y(q[0])  
        qc.swap(q[1],q[0])     
        qc.h(q[2])
        '''
        qc.h(q[2])
        qc.cx(q[1],q[2])
        qc.tdg(q[2])
        qc.cx(q[0],q[2])
        qc.t(q[2])
        qc.cx(q[1], q[2])
        qc.h(q[2])
        '''
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
