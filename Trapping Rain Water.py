#06/01/2023, Trapping Rain Water
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trap(height):
    #store trapped water in int trapped
    trapped=0
    i=0
    #iterate thru elevation map array height using int i
    while i<len(height)-1:
        #store current index as barrier to see how much water
        #it will trap
        barrier=i
        #iterate until it cannot trap anymore water
        #adding the difference in height between the barrier and area surrounding it
        #if item is largest in list do not iterate thru list as it cannot trap water
        while i<len(height) and height[barrier]>height[i+1] and (max(height[barrier:])!=height[barrier] or height[barrier:].count(height[barrier])>1):
            trapped+=height[barrier]-height[i+1]
            i+=1
        i+=1
    return(trapped)
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
