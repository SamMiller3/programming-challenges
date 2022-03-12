#Parse Integer, 12/03/2022
#Input a string s and will parse for integers
#Example input: "   these are 42 words"
#Example output: "42"
#--VARIABLES--:

s="   these are 42 words"
i=0

#--MAIN CODE--:

#iterate through string
while i<len(s):
    #if character at current index is not numeric do not parse it
    if not s[i].isnumeric():
        s = s[:i] + s[(i+1):]
    else:
        #otherwise leave it in the string
        i+=1
#output string
print(s)
