#quicksort 13/02/2022
#--Variables--:

#get user to input array
arr = input("input array of numbers to be sorted")
#convert string to list
arr = arr.split()
#convert list of string to list of int
arr = list(map(int, arr))

#--Main Code--:
def divide(arr, low, high):
    #set index
    i = low-1
    #pivot is last item in list
    pivot = arr[high]
    #sort list
    for j in range(low, high):
        #is number greater than pivot
        if pivot <= arr[j]:
            #if so then increment index and sort behind it
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #return index
    return(i+1)
        
def quickSort(arr, low, high):
    #if only 1 item in the array it is already sorted
    if high == 0:
        return arr
    if low < high:
        index = divide(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)

quickSort(arr, 0, len(arr)-1)
print(f"sorted array is: {arr}")
