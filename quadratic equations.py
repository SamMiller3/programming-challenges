offsety = "null"
div = "null"
while offsety != "bottom" and offsety != "top":
    offsety = input("start from bottom or top of screen: ")
while div != "true" and div != "false":
    print("divide output by 100? displays more on screen but trades off accuracy (reccomended for big equations but not for smaller/linear ones)")
    div = input("input either true of false: ")
if div == "true":
    div = 100
if div == "false":
    div = 1
#formula example: y=10^3x + -2^3 + 2    example formula y=(ax)^b + (cx)^d + e
print("example formula y=ax^b + cx^d + e")
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))
d = int(input("value of d: "))
e = int(input("value of e (y intercept): "))
repeat = int(input("how many increments? "))
from turtle import *
pu()
setx(0)
if offsety == "bottom":
    offsety = -450
if offsety == "top":
    offsety = 450
sety(offsety)
pd()
i=0
print("start")
print(i<repeat)
setx(1)
while i<repeat:
    print((a*xcor()**b + c*xcor()**d + e)/div)
    sety((a*xcor()**b + c*xcor()**d + e + offsety)/div)
    setx(xcor()+1)
    i+=1
print("end")


