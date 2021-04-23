#Insertion Sort Revised, 23/04/2021
#I made a buggy version of insertion sort a month and a half ago so
#I decided to start from scratch and code a new one!
#example input:
#248 43 8 2
#example output:
#2 8 43 248
pr = input("print proccess (T,F)?")
def sort(arr):
    i = 0
    while arr[0] > arr[1]:
        i = 0
        while i < len(arr)-1:
            while arr[i] > arr[i+1]:
                if arr[i] > arr[i+1]:
                    #move element to the right
                        arr.insert(i+2,arr[i])
                        arr.pop(i)
                        if pr == "T":
                            print(arr)
                if arr[i] < arr[i-1]:
                    #move element to the left
                        arr.insert(0,arr[i])
                        arr.pop(i+1)
                        if pr == "T":
                            print(arr)
            i+=1
        #do recursion if list is not sorted
        i = 0
        while i < len(arr)-1:
            if i < len(arr)-1:
                if arr[i] > arr[i+1]:
                    sort(arr)
                    break
            i+=1
#get input
arr = input("input an array of numbers: ")
#split the numbers
arr = arr.split()
#convert from strings to integers
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
#start sorting
sort(arr)
#output
print(arr)
    
                    
