#Jump Game, 19/04/2021, challenge from google/leetcode
#Explanation
#You are given an array of non negative integers
#your initially positioned at the first index of the array.
#each number jumps you that far
#determine if you are able to reach the last index.
#Input: nums = 2 3 1 1 4
#Output: true
nums = input("input an array of numbers")
nums =nums.split()
print(nums)
i = 0
completed = "false"
while True:
    if i == len(nums)-1:
        completed = "true"
        break
    if int(nums[i]) == 0:
        completed = "false"
        break
    i+=int(nums[i])
print(completed)
    
