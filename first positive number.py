nums = list(input("input an array of numbers"))
nums.sort()
for i in range(len(nums)):
    if int(nums[i]) % 2 == 0:
        print(nums[i])
        break
    
