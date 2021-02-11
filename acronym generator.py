#acronym generator
inpt = input("input a few words to be converted to an acronym")
acn = inpt[0]
i = 0
while i < len(inpt):
    i+=1
    if inpt[i-1] == " ":
        acn = acn + inpt[i]
print(acn)
