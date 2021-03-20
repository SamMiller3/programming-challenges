#median of two arrays - challange from leetcode.com
nums1 = list(input())
nums2 = list(input())
nums = nums1 + nums2
nums.sort()
if len(nums)/2 % 2 == 0:
    print("median is: " + str(nums[round(len(nums)/2)-1]) + ", " + str(nums[round(len(nums)/2)]))
else:
    print("median is: " + str(nums[len(nums)/2]))
