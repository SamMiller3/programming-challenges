#25/12/2022, Longest Subsequence With Limited Sum
#You are given an integer array nums of length n, and an integer array queries of length m.
#Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
#example:
#Input: nums = [4,5,2,1], queries = [3,10,21]
#Output: [2,3,4]
answer=[]
nums = [1000000]
queries = [1000000]
#sort nums since order of subsequence does not matter
nums.sort()
#iterate thru queries
for i in range(len(queries)):
    #iterate thru nums to find target (queries[i])
    #if the sum of nums is less than or equal to its target output
    #the length of queries
    if queries[i]>=sum(nums):
        answer.append(len(nums))
        continue
    j=0
    while sum(nums[:j]) <= queries[i]:
        j+=1
    j-=1
    answer.append(j)
print(answer)
