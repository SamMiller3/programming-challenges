#Longest Valid Parenthesis , 05/02/2023
#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring

#Example 1:
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".

#Example 2:
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".

#Example 3:
#Input: s = ""
#Output: 0



#input
s = ")(" 
#number of hanging open brackets
openBra=0
#number of hanging close brackets
closeBra=0
for i in range(len(s)):
    #increment int openBra if an open bracket is found
    if s[i]=="(":
        b+=1
    if s[i]==")":
        #if a close bracket is found and there
        #are current hanging open brackets decrase number
        #of hanging open brackets, since it is no longer hanging
        #else increase number of hanging closed brackets
        if b>0:
            b-=1
        else:
            c+=1
#return length of s take away number of hanging brackets
print(len(s)-abs(b)-c)
