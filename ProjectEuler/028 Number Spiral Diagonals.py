# Problem 28: Number Spiral Diagonals
# 25/06/2025

diagonal_sum=1 
last_term=1 # initialise to start at first position
difference=2 # difference between each vertex on the square as it expands is intially 2
# and increases by 2 each time, forming an arithmetic series of 4 terms, with first term being 
# the last term of the previous + the new difference for each square
while difference<1001:
    series_sum = 2*(2*(last_term+difference) + 3*difference) # find sum of verticies for current square
    # by summing arithmetic series
    diagonal_sum += series_sum
    last_term = last_term + 4*difference # find new last term
    difference+=2
print(diagonal_sum)

