#Longest Valid Parentheses challenge from leetcode.com, 24/03/2021
par = input("input parentheses array: ")
e = 0
j = 0
i = 0
while i < len(par):
    if e == 0 and par[i] == "(":
        e=1
        j+=1
    elif e == 1 and par[i] == ")":
        e=0
        j+=1
    else:
        e=0
    i+=1
print(j)
