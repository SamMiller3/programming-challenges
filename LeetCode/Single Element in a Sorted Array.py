# Single Element in a Sorted Array, 21/02/2023
# Leetcode: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Given a sorted array where every element appears exactly twice except for one,
# return the single element. Must run in O(log n) time and O(1) space.

def single_non_duplicate(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Make sure mid is even to compare pairs properly
        if mid % 2 == 1:
            mid -= 1

        # If the pair matches, the single element is after mid
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return nums[left]


# Example usage:
print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Output: 2
print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))    # Output: 10
