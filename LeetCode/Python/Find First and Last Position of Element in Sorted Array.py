# Problem: Find First and Last Position of Element in Sorted Array
# Date: 04/01/2023
# Given a sorted list 'nums' and a target, return the indices of the first
# and last occurrence of that target. If target not found, return [-1, -1].

def search_range(target, nums):
    if target not in nums:
        return [-1, -1]

    first = nums.index(target)
    last = len(nums) - 1 - nums[::-1].index(target)
    return [first, last]


# Example usage
print(search_range(8, [5, 7, 7, 8, 8, 10]))  # Output: [3, 4]
