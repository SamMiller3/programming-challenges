#214. Totient Chains from Project Euler
#04/11/2024

import math


def compute_totients(n):
    # Initialize an array where index i holds the value of totient(i)
    totients = list(range(n + 1))  # Start with totients[i] = i

    # Implement the sieve
    for i in range(2, n + 1):
        if totients[i] == i:  # i is a prime number
            for j in range(i, n + 1, i):
                totients[j] *= (i - 1)
                totients[j] //= i

    return totients

n = 40000000

totients=compute_totients(n) # calculate first n totients so when calculating totient chains the same totient does not need to be calculated more than once
print("totients computed")

# calculate primes up to n 

sieve = [True]*n
sieve[0]=sieve[1]=False
for i in range(2,math.isqrt(n)+1):
    if sieve[i]==True:
        for j in range((i*i),n,i):
            sieve[j]=False
print("primes marked")
primes=[]
for i in range(len(sieve)):
    if sieve[i]:
        primes.append(i)
print("primes generated")


sum=0 # value to store the sum of primes with totient chain length 25
hash={
    1: 1,
    2: 1
} # hash table to store the length of the nth totient chain, so the same chain does not need to be recalculated

for p in primes:

    chain=[p] # first value of chain is the current prime
    end=True # when end is True continue loop to find totient chain, if it is False break
    hashed=False # store if loop has been cut short as length of totient chain of current value is stored in hash table  
    len_of_chain=0
    
    while end:
        chain.append(totients[chain[-1]]) # add totient of current value to chain
        if chain[-1]==1: # if at 1 break
            end=False
        if chain[-1] in hash:
            len_of_chain=len(chain)+hash[chain[-1]] # if in hash then stop calculating totient chain
                                                    # and store length of current chain + hashed value
            hashed=True # flag as hashed and end loop 
            end=False

    if hashed==False:  # if not hashed just stop length of chain as the length of the chain calculated 
        len_of_chain=len(chain)
    if len_of_chain==25: # if length of chain is 25 add the prime at begining of chain to the sum
        sum+=p

    not_hashed = [item for item in chain if item not in hash] # check items in chain that have not been hashed yet

    for hash_value in not_hashed:
        hash[hash_value]=len(chain[chain.index(hash_value):])+1 # add them and the length of their corresponding chain to the hash

print(sum)