#rotate array, challenge from leetcode.com. 23/06/2021
array = list(input("input array"))
iterations = int(input("iterations"))
print(array)
for i in range(iterations):
    array.insert(0, array[len(array)-1])
    array.pop(len(array)-1)
    print(array)
