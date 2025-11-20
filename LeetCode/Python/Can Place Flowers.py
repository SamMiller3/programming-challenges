# Problem: Can Place Flowers
# Date: 01/04/2023
# You are given a flowerbed (array) containing 0s (empty) and 1s (planted).
# A flower cannot be planted in adjacent plots. Given an integer n,
# return True if n new flowers can be planted without violating the rule.

flowerbed = [1, 0, 0, 0, 0, 0, 1]
n = 0

need_to_plant = n
i = 0

# Check if can plant at the end
if flowerbed[-1] == 0 and flowerbed[-2] == 0:
    need_to_plant -= 1

# Check if can plant at the beginning
if flowerbed[0] == 0 and flowerbed[1] == 0:
    need_to_plant -= 1
    i += 2

# Check inner plots
while i < len(flowerbed) - 1 and need_to_plant > 0:
    if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
        need_to_plant -= 1
        flowerbed[i] = 1  # mark as planted to avoid overlap
        i += 2
    else:
        i += 1

print(need_to_plant <= 0)
