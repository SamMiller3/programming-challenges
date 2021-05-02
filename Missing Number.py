#Missing Number, 2/05/2021, problem from leetcode.com
#https://leetcode.com/problems/missing-number/
#example input: 101
#example output: 2
nums = input("input numbers")
nums1 = list()
for i in range(len(nums)):
    nums1.append(str(i))
for i in range(len(nums)):
    try:
        nums1.remove(nums[i])
    except:
        continue
print(', '.join(nums1))
