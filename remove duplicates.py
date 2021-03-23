#remove duplicates from array, 23/03/2021
array = list(input("input: "))
duplicates = list()
i = 0
while i < len(array):
    if array[i] in duplicates:
        array.pop(i)
        i-=1
    else:
        duplicates.append(array[i])
    i+=1
print(array)
