#Longest Palidromic Substring, 07/03/2022
#Challenge from leetcode.com
#Given a string s, return the longest palindromic substring in s
#Example input: s = "babad"
#example output: "bab"

#--Variables:--

s="cbbd"
sub=""
array=[]

#--Code:--

#iterate through string s
for i in range(len(s)):
    sub=""
    #starting from each index iterate from there
    #finding longest palindromic substring
    for j in range(i,len(s)):
        sub=sub + s[j]
        #check if substring is palindromic
        if sub == sub[::-1]:
            #if it is add substring to array
            array.append(sub)
#output longest string in array
print(max(array,key=len))
    
