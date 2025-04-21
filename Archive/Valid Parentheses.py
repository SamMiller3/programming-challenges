#Valid Parentheses challenge from leetcode.com, https://leetcode.com/problems/valid-parentheses/
#09/06/2022
s="(]"
for i in range(len(s)):
    if s[i] == "(" and s[i+1]!=")":
        print("false")
        break
    elif s[i] == "[" and s[i+1]!="]":
        print("false")
        break
    elif s[i] == "{" and s[i+1]!="}":
        print("false")
        break
    if i == len(s)-1:
        print("true")

