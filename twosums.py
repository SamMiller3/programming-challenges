#twosum question from leetcode.com
#input an array of numbers then a target then the program will output the index of which 2 numbers add up to make the target (presuming there is only 1)
#note this example is heavily unoptimized, you can't enter 2 digit numbers, if the numbers are in a strange order it wont be able to find the answer
i = 0
c = 0
c1 = 1
nums = list(input(""))
target = int(input(""))
while i<len(nums)-1:
    if int(nums[c])+int(nums[c1]) == target:
        print("[" + str(c) + "," + str(c1) + "]")
        break
    else:
        c+=1
        c1+=1
        i+=1
print("end")
