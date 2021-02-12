#encrypter took me ~ 1-2 hours (projects normally take ~5-15 mins)
import random
chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
while 1>0:
    crypt = ""
    while crypt != "encrypt" and crypt != "decrypt":
        print ("do you want to encrypt a message or decrypt? (enter encrypt to encrypt, decrypt to decypt)")
        crypt = input("do you want to encrypt a message or decrypt?")
    print("characters accepted: lowercase letter, uppercase letters, digits 0-9, spaces.")
    msg = input("input your message")
    if crypt == "encrypt":
        key = random.randint(100, 100000)
        print ("your key is: " + str(key))
        print("you will need your key to decrypt your message")
        i = 0
        emsg = ""
        while i < len(msg):
            foo = int(str(chars.index(msg[i])))
            foo = foo * key
            foo = foo + key
            print(foo)
            emsg = emsg + str(foo)
            emsg = emsg + ";"
            i+=1
        print("encrypted message: " + emsg)
    if crypt == "decrypt":
        key = int(input("input your key"))
        emsg = msg
        omsg = ""
        i = 0
        emsg = str(emsg)
        while i <= len(emsg)-1:
            num = ""
            while emsg[i] != ";":
                num = num + emsg[i]
                i +=1
            num = int(num) - key
            num = int(num) / key
            omsg = omsg + chars[int(num)]
            i+=1
        print ("your message has been decrypted: " + omsg)
        
        
        
