# Trapping Rain Water, 06/01/2023
# Leetcode: https://leetcode.com/problems/trapping-rain-water/
# Given an elevation map, compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max = right_max = 0
    trapped = 0

    while left < right:
        if height[left] < height[right]:
            # Water is bounded by the tallest on the left
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped += left_max - height[left]
            left += 1
        else:
            # Water is bounded by the tallest on the right
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped += right_max - height[right]
            right -= 1

    return trapped


# Example usage:
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
