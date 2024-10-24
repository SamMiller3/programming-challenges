#Project Euler - 10. Summation of Primes
#23/10/2024

import math

n = 2000000 
sieve = [True] * n  
sieve[0] = sieve[1] = False  

# Sieve of Eratosthenes
for i in range(2, math.isqrt(n) + 1):
    if sieve[i]:  # If i is still marked as prime
        for j in range(i * i, n, i):  # Mark multiples of i as non-prime
            sieve[j] = False

# Collect all primes into a list
primes = [i for i, is_prime in enumerate(sieve) if is_prime]


print(sum(primes))
