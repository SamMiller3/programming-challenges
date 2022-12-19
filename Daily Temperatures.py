#Daily Temperatures
#Given an array of integers temperatures represents the daily temperatures, return an array answer such that
#answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
#If there is no future day for which this is possible, keep answer[i] == 0 instead.
#Example 1:
#Input: temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]

temperatures=[89,62,70,58,47,47,46,76,100,70]
stack=temperatures
ans=[]
#iterate thru list tempreatures
for i in range(len(temperatures)):
    #store current value of stack in integer n
    n=stack[0]
    j=1
    #iterate thru stack until at a tempreature greater than n
    #storing number of days passed in integer j
    try:
        while stack[j]<=n:
            j+=1
    except:
        j=0
    #append n to list of days
    ans.append(j)
    #remove first item from stack so it can be ignored in future iterations
    stack.pop()
#return answer
print(ans)
