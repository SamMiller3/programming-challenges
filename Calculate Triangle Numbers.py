#Calculate Triangle Numbers, 05/05/2021
index = int(input("calculate up to what index? "))
j=0
nums=[]
for i in range(index):
    j+=i+1
    nums.append(j)
print(nums)
    
