#25/10/2024
#Project Euler - Power Digit Sum 


power=2**1000
sum=0
for digit in str(power):
    sum+=int(digit)
print(sum)
