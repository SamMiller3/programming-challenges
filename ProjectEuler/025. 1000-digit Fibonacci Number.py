# Project Euler problem 25 1000-digit Fibonacci Number 

# First approach I wrote in Septemember 2024. A bit unconventional using a binary search paired with
# Binets formula to minimise time and space complexity. It would be very efficient if it wasn't for 
# Binet's formula having overflow errors for huge values of n.

import math

def calcNthFib(n):
    # Binet's formula
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n / math.sqrt(5)) + 0.5)

def find_index_with_digits(d):
    lower = 1
    upper = 2
    # Exponential search for an upper bound
    while len(str(calcNthFib(upper))) < d:
        lower = upper
        upper *= 2

    # Binary search within range [lower, upper]
    while lower <= upper:
        mid = (lower + upper) // 2
        if len(str(calcNthFib(mid))) < d:
            lower = mid + 1
        else:
            upper = mid - 1

    return lower

if __name__ == "__main__":
    target_digits = 1000
    index = find_index_with_digits(target_digits)
    fib_num = calcNthFib(index)
    print(f"Index: {index}, Fibonacci Number: {fib_num}")

# Revised approach (standard method) 21/06/2025 using recurrence relation

a,b=1,1
i=0
while len(str(a))!=1000:
    a,b=a+b,a
    i+=1
print(i+2)