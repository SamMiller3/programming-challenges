#standard devation, 22/03/2022
#--libraries:--

import math

#--variables:--

a=[1,2,2.5]
l=[]

#--main code:--

#calculate mean of a
mean=sum(a)/(len(a))
#iterate thru a
for i in range(len(a)):
    #append the difference between current index of a and the mean to the power of 2
    l.append((a[i]-mean)**2)
print(f"variance: {sum(l)/(len(l))} standard deviance: {math.sqrt(sum(l)/(len(l)))}")
