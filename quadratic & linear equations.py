#quadraction & linear equations, first made December 2021.
#Declare variables
offset_y = "null"
divide_by_100 = "null"
#set offset_y, if your going doown it's good to start from the top otherwise start from the bottom
while offset_y != "bottom" and offset_y != "top":
    offset_y = input("start from bottom or top of screen: ")
#divide value by 100? (useful for big equations)
while divide_by_100 != "true" and divide_by_100 != "false":
    print("divide_by_100ide output by 100? displays more on screen but trades off accuracy (reccomended for big equations but not for smaller/linear ones)")
    divide_by_100 = input("input either true of false: ")
if divide_by_100 == "true":
    divide_by_100 = 100
if divide_by_100 == "false":
    divide_by_100 = 1
#formula example: y=10^3x + -2^3 + 2    example formula y=(ax)^b + (cx)^d + e
print("example formula y=ax^b + cx^d + e")
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))
d = int(input("value of d: "))
e = int(input("value of e (y intercept): "))
#how many times it will repeat
repeat = int(input("how many increments? "))
#import drawing function
from turtle import *
pu()
setx(0)
#goes to starting position
if offset_y == "bottom":
    offset_y = -450
if offset_y == "top":
    offset_y = 450
sety(offset_y)
pd()
i=0
print("start")
print(i<repeat)
setx(1)
#executes equation
while i<repeat:
    print((a*xcor()**b + c*xcor()**d + e)/divide_by_100)
    sety((a*xcor()**b + c*xcor()**d + e + offset_y)/divide_by_100)
    setx(xcor()+1)
    i+=1
print("end")
