#Solve Quadratic Equations, 25/11/2022
import cmath
def solveEqu(a,b,c):
    #use the quadratic equation to solve
    print(f"solution 1: {(-b+cmath.sqrt((b**2)-(4*a*c))/(2*a))}")
    print(f"solution 2: {(-b-cmath.sqrt((b**2)-(4*a*c))/(2*a))}")
#prompt input of quadratic equation
#example input x2+4x+4
#example output
eq=input("input quadratic equation: ")

#scrape text for vars
i=0
_=""
#a will be until first x
while eq[i] != "x":
    _=eq[i]
    i+=1
i+=3
j=i
__=""
#b will be until second x
while eq[j]!="x":
    __=eq[i:j+1]
    j+=1
j+=2
i=j
#rest of var is c
___=eq[i:]
#cast to ints
if len(_)==0:
    _=1
if len(__)==0:
    __=1
_=int(_)
__=int(__)
___=int(___)
#run quadratic equation
solveEqu(_,__,___)
