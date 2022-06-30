#Longest Palindromic Substring, 30/06/2022
#Given a string s, return the longest palindromic substring
#Example Input: s="babad"
#Example Output: s="bab"

#---Variables---:

s="babad"
#store all substrings in list strings
strings=[]

#---Main Code---:

#iterate over each item in the list
for i in range(len(s)):
    #iterate over each item in the list starting from int i
    for j in range(i,len(s)+1):
        #slice string s between i and j+1 and store in variable _
        #to create substring
        _=s[i:j+1]
        #if substring is palindromic store in strings
        if _[::-1]==_:
            strings.append(_)
#output longest item in list
print(max(strings,key=len))
