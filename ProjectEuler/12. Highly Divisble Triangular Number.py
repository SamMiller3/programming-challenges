#24/10/2024
#Project Euler - Highly Divisible Triangular Number

import math

i=7
n=28

while True:
    i+=1
    n+=i
    numDivisors=0
    for j in range(2,math.isqrt(n)+1):
        if n%j==0:
            numDivisors += 2 if j != n // j else 1
    if numDivisors>=500:
        print(f"{n}: number of divisors - {numDivisors}")
        break

