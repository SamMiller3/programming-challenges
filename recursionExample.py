#Recursion Example, 10/04/2021
def count(n):
    if 0 < n:
        print(n)
        count(n-1)
    else:
        return(n)
number = int(input("input a number"))
count(number)
