import sys
print ("Iron TextOS by Samuel Miller 13/01/2021\n")
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
        filenames.insert(len(filenames)+1, inpt)
        filetext.append("null")
        print ("file created, edit it using the EDIT cmd")
    if inpt=="EDIT":
        name = input("input a name")
        i = 0
        while name != filenames[i]:
            i=i+1
            if i>len(filenames):
                break
        if name != filenames[i]:
            print ("file not found")
        elif name == filenames[i]:
            inpt= input("input text to replace with")
            filetext[i] = inpt
            print (name + " has been edited")
    if inpt=="READ":
        name = input("input a name")
        i = 0
        while name != filenames[i]:
            i=i+1
            if i>len(filenames):
                break
        if name != filenames[i]:
            print ("file not found")
        elif name == filenames[i]:
            print (filenames[i] + " :\n" + filetext[i])
    if inpt=="RENAME":
        name = input("input name of file you want to rename")
        i = 0
        while name != filenames[i]:
            i=i+1
            if i>len(filenames):
                break
            if name != filenames[i]:
                print ("file not found")
        inpt = input("input new name")
        filenames[i] = inpt
        print(name + "has been changed to" + inpt)
    if i==repeat:
            print ("command does not exist")    
        
    
