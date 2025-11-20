# Problem: Longest Subsequence With Limited Sum
# Date: 25/12/2022
# Given an array 'nums' and a list of 'queries',
# return a list where each element is the length of the longest subsequence
# such that the sum is <= queries[i].
# A subsequence can exclude elements, but order must be preserved.

nums = [1000000]
queries = [1000000]
answer = []

# Sort to prioritize small values for max-length subsequence
nums.sort()

for q in queries:
    if q >= sum(nums):
        answer.append(len(nums))
        continue

    total = 0
    count = 0
    for num in nums:
        if total + num <= q:
            total += num
            count += 1
        else:
            break
    answer.append(count)

print(answer)
