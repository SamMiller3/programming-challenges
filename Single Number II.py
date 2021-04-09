#Single Number II
#Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
#example input:
#1 1 5 1
#example output:
#5
nums = input()
nums = nums.split()
store = list()
overThree = list()
i = 0
while i < len(nums):
    store.append(nums[i])
    if store.count(nums[i]) == 3:
        overThree.append(nums[i])
    i+=1
i=0
numsCopy = nums
while 1 != len(numsCopy):
    if numsCopy[0] in overThree:
        numsCopy.pop(0)
    elif numsCopy[1] in overThree:
        numsCopy.pop(1)
print(numsCopy)
    
