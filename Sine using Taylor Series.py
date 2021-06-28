#Calculating sine using Taylor series, 28/06/2021
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
