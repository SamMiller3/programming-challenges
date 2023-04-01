#01/04/2023, Can Place Flowers
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
#and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#example input:
#Input: flowerbed = [1,0,0,0,1], n = 1
#Output: true

flowerbed=[1,0,0,0,0,0,1]
n=0

#store number of flowers needed to plant
needToPlant=n
i=0
#base cases
#--
#check if can plant in first plot
if flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0:
    needToPlant-=1
#check if can plant in last plot
if flowerbed[0]==0 and flowerbed[1]==0:
        needToPlant-=1
        i+=2
#--
while i <len(flowerbed)-2 and needToPlant!=0:
    #check if current index is empty, and surrounding plots are empty
    #if so 1 less plant is needed to plant
    #and increment move along 2 plots
    #otherwise move along by 1 plot
    if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
        needToPlant-=1
        i+=1
    i+=1
#if enough plants have been planted return true
#otherwise return false
if needToPlant<=0:
    print(True)
else:
    print(False)
