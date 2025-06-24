# 19/04/2025 
# Project Euler - Amicable Numbers

import math

divisors_sum = 0
divisors_sum_list = []
amicable_sum = 0

for i in range(1, 10000):
    divisors_sum = 1

    bound = int(i**0.5)
    for j in range(2, bound + 1):
        if i % j == 0:
            divisors_sum += j  # Add divisor j
            if j != i // j:
                divisors_sum += i // j

    # Add to list then check the list to find amicable pairs
    divisors_sum_list.append(divisors_sum)

    if len(divisors_sum_list) > divisors_sum and divisors_sum_list[divisors_sum - 1] == i:
        amicable_sum += i + divisors_sum

print(amicable_sum)
