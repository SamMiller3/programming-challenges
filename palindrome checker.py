#palindrome checker
while 1>0:
    inpt = input("input a word/number")
    i = 0
    bckwrds = ""
    while i < len(inpt):
        bckwrds = inpt[i] + bckwrds
        i+=1
    if bckwrds == inpt:
        print ("is a palindrome")
    else:
        print ("is not a palindrome")
        
