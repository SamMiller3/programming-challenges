#bubblesort? big-o-noation algorithm, created 28/03/2021 (ascending)
list = list(input("input a base 10 array of integers to be sorted into ascending order"))
j = 0
while j < len(list)/3:
    pivot = len(list)-1
    temp = pivot-1
    i = 0
    worked = 0
    while i<len(list):
        print(str(pivot) + str(list[pivot]) + list[temp])
        if list[pivot] <= list[temp]:
            temp -=1
            i+=1
        else:
            worked = 1
            list.insert(temp+2, list[pivot])
            list.pop(pivot+1)
            if i == 0:
                    pivot-=1
                    temp-=2
            break
    if worked == 0:
        worked = 1
        list.insert(temp+2, list[pivot]) 
        list.pop(pivot+1) 
    c = 1
    temp-=1
    while c < len(list):
        temp = pivot-1
        i = 0
        worked = 0
        while i<len(list):
            print(temp)
            if list[pivot] <= list[temp]:
                temp -=1
                i+=1
            else:
                worked = 1
                if str(temp)[0] == "-":
                    list.insert(str(temp)[1]+1, list[pivot])
                else:
                    list.insert(temp+1, list[pivot])
                list.pop(pivot+1)
                if i == 0:
                    pivot-=1
                    temp-=2
                break
        if worked == 0:
            worked = 1
            list.insert(temp+1, list[pivot]) 
            list.pop(pivot+1) 
        c+=1
        
    j+=1
print(list)
