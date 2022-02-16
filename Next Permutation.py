#Next Permutation, 16/02/2022
#The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
#example input: nums = [1,2,3]
#example output: [1,3,2]
#---VARIABLES:---
nums=input("input array of nums")
nums = nums.split()
nums = list(map(int, nums)).
i = len(nums)-1
#---MAIN CODE:---
while True:
    #if length of array is 1 return it
    if len(nums) == 1:
        print(nums)
    #if length is greater than 1, find next permutation
    if nums[i] > nums[i-1] or( nums[i]== nums[i-1] and i==1):
        nums[i], nums[i-1] = nums[i-1], nums[i]
        print(nums)
        break
    else:
        i-=1
