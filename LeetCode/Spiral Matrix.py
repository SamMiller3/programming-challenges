# Spiral Matrix, 24/01/2024
# Leetcode: https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements of the matrix in spiral order.

def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:
        # Traverse from left to right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse downwards
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        # Traverse from right to left
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

        # Traverse upwards
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# Example usage:
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print(spiral_order(matrix))
# Output: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
