i = 1
try:
    lifespan = int(input("how many iterations?"))
except:
    print("enter a valid base-10 Value")
    lifespan = int(input("how many iterations?"))
while i<lifespan:
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)
    i+=1

    
