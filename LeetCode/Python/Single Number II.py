# Single Number II, 09/04/2021
# Leetcode: https://leetcode.com/problems/single-number-ii/
# Every element appears three times except one. Find that one.

from collections import Counter

def single_number(nums):
    # Count frequency of each number
    count = Counter(nums)

    # Return the number with frequency 1
    for num, freq in count.items():
        if freq == 1:
            return num


# Example usage:
nums = [1, 1, 5, 1]
print(single_number(nums))  # Output: 5
