#median of 2 sorted arrays, 13/05/2022
#challenge from leetcode.com https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
import math
#array 1
nums1=[1,3,4]
#array 2
nums2=[2,5]
#concatenate arrays
l=nums1+nums2
#sort
l.sort()
#if length of array is even then output median as length of array/2 and length of array/2-1
#if length of array is odd then output median as length of array/2-1
if len(l)%2==0:
    if not ((l[round(len(l)/2)-1]) and (l[round(len(l)/2)])) == 0:
        print((l[round(len(l)/2)-1])+(l[round(len(l)/2)]))/2
    else:
        print(0)
else:
    print(l[math.ceil(len(l)/2)-1])
