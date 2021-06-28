#Calculating sine using Taylor series, 28/06/2021
import math
import matplotlib.pyplot as plt
start = int(input("input start number"))
end = int(input("input end number"))
step = float(input("input step"))
i = start
while i < end: 
    n=3
    answer=i
    for j in range(10):
        answer-=(i**n)/math.factorial(n)
        n+=2
        answer+=(i**n)/math.factorial(n)
        n+=2
    plt.scatter(i,answer,linestyle='--', color='r')
    i+=step
plt.show()
