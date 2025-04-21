#number guessing game using psuedo random number generator 30/04/2022
#example program for my psuedo rng
#---libraries:---
import ctypes
#---functions:---
def genRanNum(chars):
    global seed
    seed= int(str(seed**2).zfill(8)[2:6])
    out=str(seed**2).zfill(8)[2:6]
    return(int(out[0:chars]))
#---variables:---
lib = ctypes.windll.kernel32
t = lib.GetTickCount64()
t = int(str(t)[:-3])
mins, seed = divmod(t, 60)
#---launch rng:---
if seed==1 or seed== 0:
    seed+=2
while len(str(seed))<4:
    seed=seed**2
#---main code:---
print("note: numbers are between 1-99")
nums=list()
while True:
    game = input("who should guess the number? (me/you)")
    if game == "me":
        num = genRanNum(2)
        print("I have thought of a number")
        ans = 0
        i = 1
        while ans == 0:
            guess = int(input("guess: "))
            if num == guess:
                print("correct! You took " + str(i) + " turns")
                ans = 1
            if num > guess and num != guess:
                print(f"the number is bigger than {guess}")
            if num < guess:
                print(f"the number is smaller than {guess}")
            i+=1
    else:
        nums.clear
        for i in range(100):
            nums.append(i)
        i=1
        midpoint = int(len(nums) / 2)
        while True:
            i+=1
            pos = input(f"is your number greater than {nums[midpoint]}? (T/F) (True/False)")
            if pos == "True" or pos == "T":
                nums = nums[midpoint:int(len(nums))]
            else:
                nums = nums[0:midpoint]
            midpoint = int(len(nums) / 2)
            if len(nums) <= 3:
                break
        j = 0
        while True:
            pos = input(f"is your numer {nums[j]}? (T/F) (True/False)")
            if pos == "True" or pos == "T":
                break
            else:
                j+=1
                i+=1
        print(f"number is {nums[j]}, I took {i} turns.")
