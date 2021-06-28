#Calculating sine using Taylor series
import math
theta = int(input("input theta"))
answer = theta
j=3
for i in range(50):
    answer-=(theta**j)/math.factorial(j)
    j+=2
    answer+=(theta**j)/math.factorial(j)
    j+=2
print(answer)
