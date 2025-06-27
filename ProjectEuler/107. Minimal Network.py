# Project Euler Problem 107. Minimal Network
# 27/06/2025

distance_matrix=[] # process text file and convert to distance matrix
with open('network.txt', 'r') as file:
    for line in file:
        row = []
        for val in line.strip().split(','):
            if val == '-':
                row.append(999999) # convert null values to 999999
            else:
                row.append(int(val))
        distance_matrix.append(row)

# find weight of network

weight=0
for i in range(1,len(distance_matrix)):
    for j in range(i):
        if distance_matrix[i][j]!=999999:
            weight+=distance_matrix[i][j]
print(weight)


# apply Prims to find MST
# look along the rows, and delete columns (by replacing with 999999)
current_row=0 # start at first row
MST_weight=0
for row in distance_matrix:
        row[0] = 999999
visited_nodes=[0]

for i in range(len(distance_matrix)-1):
    # find next node
    distance=999999
    for node in visited_nodes:
        if distance>min(distance_matrix[node]):
            distance=min(distance_matrix[node])
            current_column=distance_matrix[node].index(distance)

    MST_weight+=distance
    visited_nodes.append(current_column)
    # eliminate current column
    for row in distance_matrix:
        row[current_column] = 999999
        
print(MST_weight)
print(weight-MST_weight)
