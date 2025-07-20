"""1618A. Polycarp and Sums of Subsequences from CodeForces
29/5/2024
 https://codeforces.com/contest/1618/problem/A

Polycarp had an array `a` of 3 positive integers. He calculated the sums of all 
non-empty subsequences and sorted the results into a new array `b` of 7 integers.

Given the sorted array `b`, restore the original array `a`.

Input:
- The first line contains an integer t (1 ≤ t ≤ 5000), the number of test cases.
- Each of the next t lines contains 7 integers b1, b2, ..., b7 in non-decreasing order.

Output:
- For each test case, print three integers: the original values a1, a2, and a3.
"""

t = int(input())  # Number of test cases

for _ in range(t):
    # Read the sorted list of 7 sums
    values = list(map(int, input().split()))
    a = values[0]
    b = values[1]
    # Since the array is sorted, the largest element must be a + b + c
    total = values[6]
    c = total - a - b  # Derive c using the total sum
    print(f"{a} {b} {c}")
