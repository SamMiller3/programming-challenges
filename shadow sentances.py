#Shadow Sentences, 17/11/2022
#shadow sentences are sentences where every word is the same length and order but without any of the same letters.
#Write a function that accepts two parameters that may or may not be shadows of each other.
#The function should return True if they are and False if they aren’t.
#example "they are round" and "fold two times"

def shadowVerify(senOne,senTwo):
    #if length of two strings are not equal, they are not shadow strings
    if len(senOne)!=len(senTwo):
        return(False)
    #iterate thru senOne to check if any characters
    #are shared with senTwo
    for i in range(len(senOne)):
        if senOne[i] in senTwo:
            return(False)
    #since function is still running no chars are shared so return True
    return(True)

#run function shadowVerify
print(shadowVerify("his friends", "our company"))
