#Permutations, 16/02/2022
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#example input: nums = [1,2,3]
#example output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#---LIBRARIES:---

import math
import random

#---VARIABLES:---

nums = input("input array of numbers")
nums = nums.split()
originalNums = nums
nums = list(map(int, nums))
out = []
out.append(nums)

#---MAIN CODE:---
while len(out) != math.factorial(len(originalNums)):
    nums = originalNums
    nums = sorted(nums, key = lambda x: random.random() )
    if nums not in out:
        out.append(nums)
print(out)
        
        
               
