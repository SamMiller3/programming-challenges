#fibonacci sequence using recursion, 22/07/2022

#---variables:---
a,b,c=0,1,0

#---functions:---

def fib(num):
    #access variables
    global a,b,c
    #add a and b, store in variable
    c=a+b
    print(c)
    #store a in b for next run
    b=a
    #store c in a for next run
    a=c
    #countdown num to keep count of how many iterations left
    num-=1
    #if num is 1 no iterations left output int c otherwise run function again
    if num >= 1:
        #run function again
        return(fib(num))
    else:
        #output c
        return(c)

#prompt input on how many iterations required
i=int(input("how many iterations do you want?"))
#return output of the function
print(fib(i))
