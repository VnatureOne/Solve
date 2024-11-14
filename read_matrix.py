
import numpy as np

import pyqiopt as pq

arr = np.load('matrix_qubo.npy')

sol = pq.solve(arr, number_of_runs=1, number_of_steps=100, return_samples=False, verbose=10)

np.save("result", sol.vector)

#print(type(sol.vector), sol.objective)y