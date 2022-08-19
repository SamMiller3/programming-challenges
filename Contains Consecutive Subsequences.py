#19/08/2022, Contains Consecutive Subsequences
#This program checks if an array nums contains at least
#2 consecutive subsequences which have a len of at least 3
#for example:
#nums = [1,2,3,3,4,5]
#output would be true because 1,2,3 and 3,4,5

#===Variables:===

#store number of Consecutive Subsequences
numConSub=0
nums=[1,2,4,7]

#===Main Program:===

#if len of nums is less than 3 it cannot contain
#consecutive subsequences with a len greater than 3
if len(nums) < 3:
    print("false")
else:
    #iterate through nums with variable until at
    #index nums-3 since subsequence must be >=len(3) 
    for i in range(len(nums)-3):
        #clear list
        l=[]
        #iterate through array creating lists
        for j in range(i+3,len(nums)):
            l.append(nums[j])
        #if list produced is consecutive then increase numConSub
        if l==list(range(min(l), max(l)+1)):
            numConSub+=1
    if numConSub>1:
        print("true")
    else:
        print("false")
