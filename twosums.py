#twoSum updated, 20/03/2022, original made 19/03/2021
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
#--VARIABLES:--

#prompt user input for array of nums and target
nums = input("input arr of nums")
target = int(input("input target"))
#convert string of nums to list
nums=nums.split()
#loop breaker variable
d=0
#list containing index of nums that add up to make target
pSum = []

#--MAIN CODE:--

#loop thru nums
for i in range(len(nums)):
    #loop thru nums each iteration of first loop
    for j in range(len(nums)):
        #if i and j add up to equal target then append them
        #to pSum, break out of loops and output
        if int(nums[i])+int(nums[j])==target and i!=j:
            #append i and j to pSum
            pSum.append(i)
            pSum.append(j)
            #set loopbreaker variable to 1
            d=1
            break
    #break out of all loops
    if d==1:
        break
#output pSum
print(pSum)
               
