#Longest Substring Without Repeating Characters, 29/01/2023
#Given a string s, find the length of the longest substring without repeating characters.

s = "pwwkew"
#store length of longest substring in int longSubStr
longSubStr=0
#iterate thru s using int i
for i in range(len(s)):
    curStr=""
    #iterate thru s from index i
    for j in range(i,len(s)):
        #if current index is not in curStr append it, else break from the loop
        #after loop ends check if it is longest str, if true store it
        if s[j] not in curStr:
            curStr=curStr+s[j]
        else:
            longSubStr=max(len(curStr),longSubStr)
            break
    longSubStr=max(len(curStr),longSubStr)
print(longSubStr)
