#my first ever python script
inpt = input("")
parse = ""
#input format: https://www.youtube.com/test (20) or https://youtu.be/ (12)
if inpt[12] == "y":
    i = 24
    while i<len(inpt):
        parse = parse + inpt[i]
        i=i+1
if inpt[8] == "y":
    i = 17
    while i<len(inpt):
        parse = parse + inpt[i]
        i=i+1
print(parse)

#GET YOUTUBE ID, sololearn.com challenge
