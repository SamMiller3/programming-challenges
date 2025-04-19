#25/10/2024
#Project Euler - Lattice Path

import numpy as np

matrix = np.zeros((20, 20))
matrix[0]=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
matrix=matrix.T
matrix[0]=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
matrix=matrix.T
for i in range(1,20):
    for j in range(1,20):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
print(matrix[-1][-1])
