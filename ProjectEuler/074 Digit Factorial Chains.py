# Project Euler Problem 74 Digit Factorial Chains
# 26/06/2025

import math
digit_facts={} # store the digit factorial sum of previous numbers to a hashmap to prevent recalculation
count=0
n=1000000

for i in range(1,n):

    if i in digit_facts:
        digit_factorial=digit_facts[i] # if current index is in hashmap look it up

    else: # otherwise calculate digit factorial sum and store to hashmap
        num=str(i)
        digit_factorial=0
        for j in range(len(num)):
            digit_factorial+=math.factorial(int(num[j]))
        digit_facts[i]=digit_factorial
    chain_length=1
    chain=[i]

    while digit_factorial not in chain: # find length of chain
        chain.append(digit_factorial)

        if digit_factorial in digit_facts:
            digit_factorial=digit_facts[digit_factorial]

        else:
            num=str(digit_factorial)
            digit_factorial=0
            for j in range(len(num)):
                digit_factorial+=math.factorial(int(num[j]))
            digit_facts[int(num)]=digit_factorial
        chain_length+=1

    if chain_length==60:
        count+=1

print(count)