#21/07/2023, Recursive QuickSort

steps=0


def quickSort(arr):

    #base case: if arr to be sorted contains 1 element or less
    #it has already been sorted
    if len(arr)<=1:
        return(arr)
    
    global steps
    steps+=1
    #uses last element as pivot
    pivot=arr[-1]
    #Utilizes list slicing to create left and right partitions 
    right,left=[],[]
    #iterate thru arr, if current index is greater than pivot
    #store on right, otherwise store on left
    for i in range(len(arr)-1):
        if arr[i]>pivot:
            left.insert(0,arr[i])
        else:
            right.insert(0,arr[i])
    #recursively sort left and right partitions
    sortedRight=quickSort(right)
    sortedLeft=quickSort(left)
    return sortedRight + [pivot] + sortedLeft
arr=[9, 47, 11, 56, 26, 55, 88, 78, 31, 16, 96, 62, 45, 15, 39, 25, 39, 2, 37, 7, 91, 6, 58, 96, 70, 44, 13, 44, 51, 41, 6,
             70, 26, 88, 13, 12, 2, 53, 56, 8, 7, 49, 10, 24, 50, 29, 89, 45, 29, 16, 45, 3, 54, 8, 35, 32, 28, 70, 55, 80, 94, 72,
             28, 88, 20, 77, 100, 94, 76, 52, 93, 51, 62, 72, 81, 77, 89, 26, 9, 82, 55, 39, 38, 41, 23, 54, 19, 23, 4, 32, 64, 88,
             1, 54, 75, 86, 54, 81, 94, 28
             ]
print(quickSort(arr))
print(f"steps: {steps}")
