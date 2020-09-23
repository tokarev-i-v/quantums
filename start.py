import numpy as np
from qiskit import *

q = QuantumRegister(3, 'q')
circ = QuantumCircuit(q)
circ.h(q[0])
circ.cx(q[0],q[1])
circ.cx(q[0],q[2])
circ.draw()
backend = BasicAer.get_backend('statevector_simulator')
job = execute(circ, backend)
result = job.result()
outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)
from qiskit.visualization import plot_state_city
plot_state_city(outputstate)