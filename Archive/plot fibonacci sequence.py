import matplotlib.pyplot as plt
import math
print("plots Fibonacci Sequence up to 5")
start = int(input("start from what number? I reccomend -5 or 0, must be less than 5 "))
i=start
arr=[]
while i < 5:
    arr.append(((1.61803398875**i) - (-1/1.61803398875)**i)/math.sqrt(5))
    i+=0.01
y = [ele.imag for ele in arr]
x = [ele.real for ele in arr]
plt.scatter(x, y)
plt.ylabel('fibonacci sequence')
plt.show()
