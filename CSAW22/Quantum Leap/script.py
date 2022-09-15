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

    #apply the CNOT gate
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

#Explain the task
#Brief introduction to quantum computing
#Explain quantum gates (Pauli gates + 2-qubit gates)
#Explain how CNOT-gate works 
#Expolit
