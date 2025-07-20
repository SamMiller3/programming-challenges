# CodeForces 702C. Cellular Network, difficulty 1500
# 20/07/25

a = input() # first line takes number of cities and towers
cities = input().split()
cities = [int(x) for x in cities] # process into list of ints
towers = input().split()
towers = [int(x) for x in towers]

r = 0 

for city in cities: 
    if len(towers)>1:
        # use binary search to find closest city
        lower = 0
        upper = len(towers)-1
        index = (upper+lower)//2
        tower = towers[index]
        while True:
            if city < tower:
                upper = index
            elif city > tower:
                lower = index
            elif city == tower:
                break
            index = (upper+lower)//2
            tower = towers[index]
            if upper-1==lower: # choose minimum distance out of upper and lower when they are the only options
                if abs(towers[upper]-city)>abs(towers[lower]-city):
                    tower=towers[lower]
                else:
                    tower=towers[upper]
                break
            elif upper==lower: # if they are equal then minimum distance has been found
                break
    else:
        tower = towers[0] # if len(towers) is 1 there is only 1 option
    distance = abs(city-tower)
    r = max(r, distance) # r must be maximum so each city can be reached
print(r)