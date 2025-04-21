#Unique Number of Occurrences, 29/04/2021
"""Given an array of integers arr, write a function that returns true
if and only if the number of occurrences of each value in the array is unique."""
#input
arr = input("input array ")
arr = arr.split()
occ = list()
letters = list()
#checks occurrences
for i in range(len(arr)):
    if arr[i] not in letters:
        letters.append(arr[i])
        occ.append(arr.count(arr[i]))
unique = False
#checks if it is unique
for i in range(len(occ)):
    if occ.count(occ[i]) > 1:
        unique = True         
        break
#output
if unique:
    print("false")
else:
    print("true")
