#Longest Valid Parentheses challenge from leetcode.com, 24/03/2021.
#Bug fix on 27/03/2021
par = input("input parentheses array: ")
e = 0
j = 0
i = 0
if len(par) > 1:
    while i < len(par):
        if i < len(par)-1:
            if e == 0 and par[i] == "(" and par[i+1] == ")":
                e=1
                j+=1
            elif e == 1 and par[i] == ")":
                e=0
                j+=1
            else:
                e=0
            i+=1
        else:
            if e == 1 and par[i] == ")":
                e=0
                j+=1
            else:
                e=0
            i+=1
print(j)
#---------------------
#old version
#Longest Valid Parentheses challenge from leetcode.com, 24/03/2021
#par = input("input parentheses array: ")
#e = 0
#j = 0
#i = 0
#while i < len(par):
#    if e == 0 and par[i] == "(":
#        e=1
#        j+=1
#    elif e == 1 and par[i] == ")":
#        e=0
#        j+=1
#    else:
#        e=0
#    i+=1
#print(j)
