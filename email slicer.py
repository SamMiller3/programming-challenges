#email slicer
while 1>0:
    inpt = input("input your email")
    username = ""
    domain = ""
    i=0
    while inpt[i] != "@":
        username = username + inpt[i]
        i+=1
    i+=1
    while i < len(inpt):
        domain = domain + inpt[i]
        i+=1
    print ("your username is: " + username + " and your domain is: " + domain)
        
    
