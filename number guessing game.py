#number guessing game,
#wrote computer guesses on 21/03/2021
#wrote you guess on 02/09/2021
import random
print("note: numbers are between 1-99")
nums=list()
while True:
    game = input("who should guess the number? (me/you)")
    if game == "me":
        num = random.randint(1,99)
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
