#21/02/2023, Single Element in a Sorted Array
#You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#Return the single element that appears only once.
#Your solution must run in O(log n) time and O(1) space.

#example input: nums = [1,1,2,3,3,4,4,8,8]
#example output: 2
#example input: nums = [3,3,7,7,10,11,11]
#example output: 10

nums = [1,1,2,3,3,4,4,8,8]

def singleNonDuplicate(nums):
        #if list is only 1 element then return that element
        #if 0th index is smaller than first index return 0th element
        #since each number will repeat, and the repeat of each number will
        #be after eachother since the array is sorted
        #so if 1st index is greater than 0th then the 0th index did not repeat
        if len(nums)==1 or nums[0]<nums[1]:
            return(nums[0])
        #if last index is greater than second last index that means last index did not repeat
        #since second last index would equal last index if it was repeated
        if nums[-1]>nums[-2]:
            return(nums[-1])
        #go up in steps of 2, since only every second element needs to be checked
        for i in range(len(nums),2):
            #if current index is greater than index behind it AND smaller than index in front
            #that means it does not repeat, so return it
            if nums[i]>nums[i-1] and nums[i+1]>nums[i]:
                return(nums[i])
print(singleNonDuplicate(nums))
