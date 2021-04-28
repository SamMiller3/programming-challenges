#Length of Last Word, leetcode.com problem, 28/04/2021
#https://leetcode.com/problems/length-of-last-word/
#example input:
#Hello World
#example output:
#5
s = input("input")
s=s.split()
print(s)
if s:
    print(len(s[len(s)-1]))
else:
    print(0)
