# 19/05/2025
# Project Euler 23. Non-Abundant Sums



def main():
    abundant_numbers = []

    # All integers greater than 28123 can be written as the sum of two abundant numbers
    # So all numbers up to 28123 need to be checked for abundance   
    # find all abundant numbers under 28123
    for i in range(1, 28123):
        divisors_sum = 1
        bound = int(i ** 0.5)

        for j in range(2, bound + 1):
            if i % j == 0:
                divisors_sum += j  # Add divisor j
                if j != i // j:
                    divisors_sum += i // j

        if divisors_sum > i:
            abundant_numbers.append(i)

    abundant_set = set(abundant_numbers)  # cast to set for constant lookup time

    non_abundant_sum = 0

    # check all numbers under 28123
    for i in range(1, 28123):
        sum_of_abundant_numbers = False

        for j in abundant_numbers:
            if j > i // 2:
                break  # if current element is over half of i, then a pair does not exist
            if i - j in abundant_set:  # check if i - j is also abundant
                sum_of_abundant_numbers = True
                break  # once found, break early

        if not sum_of_abundant_numbers:
            non_abundant_sum += i  # otherwise, increment sum by i

    print(non_abundant_sum)


if __name__ == "__main__":
    main()
