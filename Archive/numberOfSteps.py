#Number of Steps, 27/05/2022
#challenge from leetcode.com, https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
num=14
i=0
while num!=0:
    if num % 2 == 0:
        num=num/2
    elif num % 2 !=0:
        num-=1
    i+=1
print(i)

