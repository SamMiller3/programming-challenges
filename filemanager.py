import sys
print ("File Manager by Samuel Miller 25/01/2021\n")
print ("type help for a list commands and info")
cmds = ["help","KILL","CREATE","READ","RENAME","EDIT"]
kill = 0
filenames = []
filetext = []
while 1>0 and kill==0:
    try:
        inpt = input("input a cmd: ")
    except EOFError as e:
        print("sorry this program could not run on this compiler, try running it on the actual python compiler.")
        exit()
    if inpt == "help":
         print ("Iron TextOS by Samuel Miller 13/01/2021\n")
         print ("type help for a list commands and info")
         print ("KILL - kills the program\nCREATE - create a file\nEDIT - edit the contents of a file\nREAD - reads the contents of a file\nRENAME - rename a file")
    if inpt == "kill":
        kill=1
        exit()
    repeat = len(cmds)
    i = 1
    while i<repeat:
        if cmds[i]==inpt:
            break
        i= i+1
    i=1
    if inpt=="CREATE":
        inpt = input("input a name")
        f = open(inpt + ".txt", "w")
        f.write("null")
        f.close()
        print ("file created, edit it using the EDIT cmd")
    if inpt=="EDIT":
        name = input("input a name")
        inpt= input("input text to replace with")
        f = open(name + ".txt", "w")
        f.write(inpt)
        f.close()
        print (name + " has been edited")
    if inpt=="READ":
        name = input("input a name")
        f = open(name +".txt", "r")
        print(f.read())
        f.close()
    if inpt=="RENAME":
        name=input("file you want to rename")
        inpt = input("input new name")
        f.rename(inpt + ".txt", name + ".txt")
        f.close()
        print(name + "has been changed to" + inpt)
    if i==repeat:
            print ("command does not exist")    
        
    
