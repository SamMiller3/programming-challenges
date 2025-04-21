#Arithmetic Slices, 4/03/2021
#Challenge from leetcode.com
#An integer array is called arithmetic if it consists of at least three elements
#and if the difference between any two consecutive elements is the same.
#For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

#--Variables:--

nums=[1,2,3,8,9,10]
noSubarrays=0
subArrays =[]

#--Code:--

#if length of array is less than 3 it contains no subarrays
if len(nums)>=3:
    #iterate through array
    for i in range(len(nums)-1):
        #find a subarray by going through the array from index i
        j = i
        dif = nums[j+1]-nums[j]
        while True:
            #if array is longer than 3 then add to number of subarrays
            if j-i >= 2:
                noSubarrays+=1
                subArrays.append(nums[i:j+1])
            if(not j>=len(nums)-1):
                #if difference is not the same between two positions in the array then stop iterating
                if nums[j+1] - nums[j] != dif:
                    break
            #if at the end of the array then stop iterating
            if(j>=len(nums)-1):
                break
            j+=1

print(f"number of subarrays: {noSubarrays}, subarrays are: {subArrays}")
 
