#Decode a String, google/leetcode challenge. 15/04/2021
#final version
#Updated 16/04/2021, would display 3[a2[c]] as aaacc instead of accaccacc. now fixed.
#sample input: 3[a]2[bc]
#sample output: aaabcbc
#sample input 2: 3[a2[c]]
#sample output 2: accaccacc
#sample input 3: 2[abc]3[cd]ef
#sample output 3: abcabccdcdcdef
#sample input 4: abc3[cd]xyz
#sample input 4: abccdcdcdxyz
s = input("input: ")
i = 0
num = 0
letters = ""
while i < len(s)-1:
    if s[i].isdigit():
        num += int(s[i])
    if s[i].isalpha():
        letters = letters + s[i]
        num = 0
    if s[i] == "[":
        t=0
        i+=1
        letters1 = ""
        while s[i] != "]":
            letters1 = letters1 + s[i]
            i+=1
            if s[i].isdigit():
                print(i)
                t=1
                break
        j = 0
        if t == 1:
            letters2 = ""
            num2 = 0
            print(s[i])
            while s[i] != "[":
                num2 += int(s[i])
                i+=1
            i+=1
            while s[i] != "]":
                letters2 = letters2 + s[i]
                i+=1
            i+=1
            while j < num:
                letters = letters + letters1
                j+=1
                ji=0
                while ji < num2:
                    letters = letters + letters2
                    ji+=1
            num = 0
        if t == 0:
            while j < num:
                letters = letters + letters1
                j+=1
            num = 0
    i+=1
print(letters)
