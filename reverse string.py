while 1>0:
    inpt=input("input a string")
    out=""
    for i in range(len(inpt)):
        out=inpt[i]+out
    print("reversed string: " + out)
