offsety = "blank"
while offsety != "bottom" and offsety != "top":
    offsety = input("bottom or top: ")
#formula example: y=10^3x + -2^3 + 2    example formula y=(ax)^b + (cx)^d + e
print("example formula y=ax^b + cx^d + e")
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))
d = int(input("value of d: "))
e = int(input("value of e: "))
repeat = int(input("how many increments? "))
from turtle import *
pu()
setx(0)
if offsety == "bottom":
    sety(-450)
if offsety == "top":
    sety(450)
pd()
i=0
print("start")
print(i<repeat)
while i<repeat:
    print((a*xcor()**b + c*xcor()**d + e))
    sety((a*xcor()**b + c*xcor()**d + e))
    setx(xcor()+1)
    i+=1
print("end")


