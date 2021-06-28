#quadraction & linear equations
#first made December 2021, revised 28/06/2021
#Declare variables
#formula example: y=10^3x + -2^3 + 2    example formula y=(ax)^b + (cx)^d + e
print("example formula y=ax^b + cx^d + e")
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))
d = int(input("value of d: "))
e = int(input("value of e (y intercept): "))
#how many times it will repeat
start=float(input("start?"))
increments = int(input("how many increments? "))
step = float(input("step?"))
#import matlib
import matplotlib.pyplot as plt
i=start
#starts plotting
while i<increments-abs(start):
    plt.scatter(i,(a*i**b + c*i**d + e),linestyle='--', color='r')
    i+=step
plt.show()
