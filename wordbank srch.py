letters = list(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","q","r","s","t","u","v","w","x","y","z"])
import random
i=0
wordslist = list()
print ("generating over 1 million words...")
while i<1000000:
    rand = random.randint(1,5)
    i1 = 1
    word =""
    while i1<rand:
        rand1 = random.randint(0,25)
        word = word + letters[rand1]
        i1+=1
    i+=1
    wordslist.append(word)
print("just a bit longer")
while True:
    inpt = input("input a value to be searched ")
    i=0
    j=0
    while i<len(wordslist)-1:
        if wordslist[i] == inpt:
            j+=1
        i+=1
    print(str(j) + " cases found of " + inpt + " worked")
