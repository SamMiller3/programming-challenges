#Binary Search, 02/09/2021
print("input array of numbers, eg: 1 4 7 8 10 12")
nums = input("input: ")
nums = nums.split()
nums = [int(item) for item in nums]
print("Now input number to find, IT MUST BE IN THE LIST")
num = int(input("input number to find"))
nums.sort
midpoint = int(len(nums) / 2)
while True:
    nums2 = nums[midpoint:int(len(nums))]
    if num in nums2:
        nums = nums2
    else:
        nums = nums[0:midpoint]
    midpoint = int(len(nums) / 2)
    if len(nums) <= 3:
        break
i = 0
while True:
    if num != nums[i]:
        i+=1
    else:
        break
print(f"number is {nums[i]}")
