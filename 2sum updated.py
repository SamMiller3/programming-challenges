#twosum updated 23/01/2022
#input an array of numbers then a target then the program will output the index of which 2 numbers add up to make the target (presuming there is only 1)
#input target example: 5
#input array example: 2 9 3
#output example: numbers are: 2 and 3
# ------------------------------------------------------------ 
# ------------------------------------------------------------ 
# Global variables 
# ------------------------------------------------------------

target = int(input("input target"))
nums = input("input array of numbers")
nums=nums.split()

# ------------------------------------------------------------ 
# Main program 
# ------------------------------------------------------------

for i in range(len(nums)):
    for k in range(len(nums)):
        if int(nums[i]) + int(nums[k])== target:
            print(f"numbers are: {nums[i]} and {nums[k]}")
            break
        
        
