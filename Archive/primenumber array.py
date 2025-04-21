iterations = int(input("how many iterations? "))
nums = list()
nums.append(3)
for i in range(3,iterations):
    if i % 2 == 0:
        continue
    if 0 == (i%3):
        print(i)
        continue
    nums.append(i)
print(nums)
