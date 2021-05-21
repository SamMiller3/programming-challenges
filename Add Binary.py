#Add Binary, 21/05/2021
bin1 = input("binary num1: ")
bin2 = input("binary num2: ")
num1 = 0
num2 = 0
for i in range(len(bin1)):
    if bin1[i] == "1":
        num1+=int(2**i)
for i in range(len(bin2)):
    if bin2[i] == "1":
        num2+=int(2**i)
print(num1+num2)
