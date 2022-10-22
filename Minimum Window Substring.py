#22/10/2022, Minimum Window Substring, problem from https://leetcode.com/problems/minimum-window-substring/
#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character
#in t (including duplicates) is included in the window.
#If there is no such substring, return the empty string "".
#The testcases will be generated such that the answer is unique.
#A substring is a contiguous sequence of characters within the string.

#Example:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

#declare variable instancesOfT which will store how many instances of t[k]
#are in a substring, if the limit is reached, the substring is correct.
instancesOfT=0
s = "ADOBECODEBANC"
t = "ABC"
#store all valid substrings in this list to find shortest at end
allSubStr=[]
#iterate through string s using int i
for i in range(len(s)):
    #iterate from point i using int j
    for j in range(i,len(s)+1):
        #slice list from i to j to create a substring
        substr=s[i:j]
        #split 
        subStrSlice=[*substr]
        #iterate thru substring to find number of instances of chars shared with target
        for k in range(len(t)):
            if t[k] in subStrSlice:
                subStrSlice.pop(subStrSlice.index(t[k]))
                instancesOfT+=1
            else:
                break
        #if instancesOfT is same as T add substring to
        #potential substring list
        if instancesOfT==len(t):
            allSubStr.append(substr)
        instancesOfT=0
#output substring with shortest length
if len(allSubStr)>0:
    print(min(allSubStr, key=len))
else:
    print("")
