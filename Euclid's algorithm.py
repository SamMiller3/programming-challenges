#Euclid's algorithm, 29/08/2021
#find gcd (greatest common divisor)
a = int(input("number 1: "))
b = int(input("number 2: "))
if a < b:
    c = a
    a = b
    b = c
while True:
    c = b
    b = a % b
    a = c
    try:
        if 0 == a % b:
            break
    except:
        break 
print(a)
