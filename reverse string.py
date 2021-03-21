#reverse string 19/01/2021, challenge from quora.com
while 1>0:
    inpt=input("input a string")
    out=""
    for i in range(len(inpt)):
        out=inpt[i]+out
    print("reversed string: " + out)
