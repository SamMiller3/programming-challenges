# Advent of Code 2025 Day 1
password = 0
num = 50 
with open("input", "r") as file:
    for line in file:
        turn = line.strip()
        direction = turn[0]
        magnitude = int(turn[1:]) 
        if direction == "L":
            num = (num - magnitude) % 100
        else:
            num = (num + magnitude) % 100
        if num == 0: password+=1
print(password)

