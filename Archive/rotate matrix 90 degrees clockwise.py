#rotate a matrix 90 degrees clockwise, 18/07/2023
matrix = [[1,2,3],[4,5,6],[7,8,9]]

#create a copy of the matrix
newMatrix = [[0] * len(matrix) for i in range(len(matrix))]

#iterate thru the matrix then at every index, swap the x and y coords
#and y coordinate being assigned will be the inverse of the
#inverse of the x coordinate being accessed
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        newMatrix[j][len(matrix)-i-1]=matrix[i][j]
print(newMatrix)
