#Count Primes, problem from leetcode.com, 28/04/2021
#https://leetcode.com/problems/count-primes/
#example input: 10
#example output: 4
n = int(input("input a number: "))
j = 0
flag = False
def isPrime(num):
    if num > 1:
        global flag
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    else:
        flag = False
for i in range(n):
    flag = True
    isPrime(i)
    if flag:
        j+=1
print(j)
