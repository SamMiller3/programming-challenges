#Single Number, 13/07/2023
#Challenge from leetcode.com
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

nums = [2,2,1]

#sort nums, so then all duplicate numbers will be adjacent to eachother
#this means when iterating thru the array nums, can step by 2
nums.sort()
for i in range(0,len(nums),2):
    if nums.count(nums[i])==1:
        return(nums[i])
