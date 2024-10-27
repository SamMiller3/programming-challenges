#Project Euler - 10. Summation of Primes
#26/10/2024

import math

n = 2000000
sieve = [True]*n
sieve[0]=sieve[1]=False
for i in range(2,math.isqrt(n)):
    if sieve[i]==True:
        for j in range((i*i),n,i):
            sieve[j]=False
sum=0
for i in range(len(sieve)):
    if sieve[i]:
        sum+=i
print(sum)
