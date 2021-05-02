#Calcalute Index of Fibonacci Sequence, 2/5/2021
#Uses Binet's Law
#((1.61803398875^n) - (-1/1.61803398875)^n)/√5
import math
n = int(input("input index to calculate: "))
print(round(((1.61803398875**n) - (-1/1.61803398875)**n)/math.sqrt(5)))
