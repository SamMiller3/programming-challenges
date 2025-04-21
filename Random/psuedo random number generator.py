#Pseudo Random Number generator 29/04/2022
#This program uses the Von Neumann middle square method
#The seed is set to the current second on the clock
#then squared until it is 4 digits long
#once a 'random' number is generated
#the number will be stored as the seed
#---libraries:---
import ctypes
#---functions:---
def genRanNum(chars):
    global seed
    #store current random number as seed so it can be reused
    seed= int(str(seed**2).zfill(8)[2:6])
    #convert output to string and remove middle
    out=str(seed**2).zfill(8)[2:6]
    #return requested number of random characters
    return(int(out[0:chars]))
#---variables:---
lib = ctypes.windll.kernel32
t = lib.GetTickCount64()
t = int(str(t)[:-3])
#sets seed to current seconds on the clock
mins, seed = divmod(t, 60)
#---main code:---
#make sure the seed is not 1 or 0 so it does
#not get stuck infinite loop
if seed==1 or seed== 0:
    seed+=2
#square seed until it is 4 digits since seed must be 4 digits
while len(str(seed))<4:
    seed=seed**2
#print 10 random numbers using random function
for i in range(10):
    #print a random number 4 chars long
    print(genRanNum(1))
