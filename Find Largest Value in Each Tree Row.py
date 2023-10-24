#Find Largest Value in Each Tree Row, 14/10/2023
#Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#example input: root = [1,3,2,5,3,null,9]
#Example output: [1,3,9]

root = [1,3,2,5,3,"null",9]

import math
largest_values=[]
j=0

#get the logarithm (base two) of the length plus 1 of root.
#this will will give the number of rows in the tree

for i in range(int(math.log(len(root)+1,2))):
    row=[]
    
    #in each row iterate 2^i times (the length of the row
    #processing each element
    
    for k in range(2**i):
        if root[j]!="null":
            row.append(root[j])
        else:
            row.append(0)
        print(row)
        j+=1
        
    #add the largest element in current row to arr for output
    largest_values.append(max(row))
print(largest_values)
