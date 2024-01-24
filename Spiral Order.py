#Spiral Matrix 24/01/2024
#Given an m x n matrix, return all elements of the matrix in spiral order.

#Example:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]



def spiralOrder(matrix):

        #dir 1 right, 2 down, 3 left, 4 up
        dir=1


        #basecase 
        if len(matrix)>1:
                
            m=len(matrix)
            n=len(matrix[0])
            
        else:
                
            return(matrix[0])

        #current pos in matrix 
        x,y=0,0

        
        result=[]

        #create new m*n matrix to transverse 
        zero_matrix = [[0 for _ in range(n)] for _ in range(m)]

        
        for i in range(n*m):

        #current coords in matrix set to zero matrix
            zero_matrix[y][x]=matrix[y][x]
            result.append(matrix[y][x])

            #if in a corner rotate
            if x==n-1 and y==0:
                dir=2
            elif x==n-1 and y==m-1:
                dir=3
            elif x==0 and y==m-1:
                dir=4

        #if not on the side then:
            elif x<n-1 and y<m-1:
                    #if going right, but next pos is taken and y below not go down 
                if zero_matrix[y][x+1]!=0 and dir==1 and zero_matrix[y+1][x]==0:
                    dir=2
                    #if going left and next pos isnt 0 and above is empty go up
                elif zero_matrix[y][x-1]!=0 and dir==3 and zero_matrix[y-1][x]==0:
                    dir=4
                    #if going up and next pos is taken and right is empty go right
                elif zero_matrix[y-1][x]!=0 and dir==4 and zero_matrix[y][x+1]==0:
                    dir=1
                    #if going down and down isnt empty but left is go left
                elif zero_matrix[y+1][x]!=0 and dir==2 and zero_matrix[y][x-1]==0:
                    dir=3

                #move in current direction
            if dir==1:
                x+=1
            elif dir==2:
                y+=1
            elif dir ==3:
                x-=1
            elif dir==4:
                y-=1
        return(result)

print(spiralOrder(
        [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        ))
