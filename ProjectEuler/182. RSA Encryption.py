# 25/04/2025 RSA Encryption
# Find the sum of values of e that give the least possible concealed messages.
# p = 1009, q = 3643.

import math

p = 1009
q = 3643
TOTIENT = (p-1)*(q-1)
n = p * q

# calculate values of e (e must be coprime with TOTIENT)
e_values = []
for i in range(1, TOTIENT):
    if math.gcd(i, TOTIENT) == 1:
        e_values.append(i)

# Calculate number of concealed messages for each e using Chinese Remainder Theorem.
# (I discovered this method through research; originally I used dynamic programming)
# The Chinese Remainder Theorem approach significantly optimised the solution.
min_concealed = (p * q)  # Initialize with a high number
number_of_min_concealed = 0

# Iterate over e values to find the least concealed messages
for e in e_values:
    num_concealed = math.gcd(e - 1, p - 1) * math.gcd(e - 1, q - 1)
    if num_concealed == min_concealed:
        number_of_min_concealed += e  # Add e to the sum if it matches the current minimum
    if num_concealed < min_concealed:
        number_of_min_concealed = e  # Reset the sum and update the minimum concealed messages
        min_concealed = num_concealed

# Output the sum of values of e that result in the least concealed messages
print(number_of_min_concealed)
