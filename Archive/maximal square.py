#19/07/2023, Maximal Square
#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

matrix = [["1","0","1","0","0"]
          ,["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
maxSide=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "1":
            #when 1 is found, find distance from edge of matrix on both x and y axis
            #then find the minimum of these 2, this provides the maximum size of the square
            xSpace = len(matrix[0]) - j
            ySpace = len(matrix) - i
            bound = min(xSpace, ySpace)
            #increase square size by 1 until size of bound.
            #each time square size is increased check if it only contains 1s thru brute force
            for k in range(1, bound + 1):
                isSquare = True
                for m in range(k):
                    for n in range(k):
                        if matrix[i + m][j + n] == "0":
                            isSquare = False
                            break
                    if not isSquare:
                        break
                #if it is a square after check, store larged side length
                if isSquare:
                    maxSide=max(maxSide,k)
#return largest square area
print(maxSide ** 2)
