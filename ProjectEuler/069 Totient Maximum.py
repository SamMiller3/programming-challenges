# 03/05/2025 Project Euler 69 Totient Maximum
# Find the value n <= 1,000,000 for which n/phi(n) is a maximum

n = 1000000

# Initialize an array where index i holds the value of totient(i)
totients = list(range(n + 1))  # Start with totients[i] = i

# Implement the sieve to find first n totients
for i in range(2, n + 1):
    if totients[i] == i:  # i is a prime number
        for j in range(i, n + 1, i):
            totients[j] *= (i - 1)
            totients[j] //= i

# Find the value n/phi(n) maximum
max_totient = 1
index = 1

for i in range(2, n):
    value = i / totients[i]
    if value > max_totient:
        max_totient = value
        index = i

print(index)
print(max_totient)
