#N-th Tribonacci Number, 30/01/2023
#The Tribonacci sequence Tn is defined as follows: 
#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#Given n, return the value of Tn.
#example input: 25
#example output: 1389537


def nTrib(a,b,c,d,i):
    #d is sum of past 3 ints
    d=a+b+c
    #take away 1 from i to store which recursion currently on
    i-=1
    #shift variables along by 1
    a,b,c=b,c,d
    #if recursed n times then return d
    #otherwise recurse again
    if i>1:
        return(nTrib(a,b,c,d,i))
    else:
        return(d)

#base case
if n==0:
    return(0)

#return output of recursive function nTrib
print(nTrib(0,0,1,0,n))
