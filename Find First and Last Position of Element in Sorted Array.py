#04/01/2023, Find First and Last Position of Element in Sorted Array
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

def searchRange(target,nums):
    #store the positions of first and last
    #instances of the target in this list
    targetPos=[]
    #store number of instances of target in nums
    instances=nums.count(target)
    if target not in nums:
        return([-1,-1])
    #iterate number of instances of target thru nums
    for i in range(instances):
        try:
            #if it is the first or last instance of target
            #then append it to list targetPos
            if instances-i==1 or i == 0:
                targetPos.append(nums.index(target)+i)
            nums.pop(nums.index(target))
        finally:
            continue
    if len(targetPos)==1:
        targetPos.append(l[0])
        return(targetPos)
    return(targetPos)
print(searchRange(8,[5,7,7,8,8,10]))
