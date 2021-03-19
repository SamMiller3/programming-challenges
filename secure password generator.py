#secure password generator
import random
import string
len = random.randint(12,16)
password = ""
i = 1
while i < len:
    password = password + chr(random.randint(33,126))
    i+=1
print (password)
