# Advent of Code 2025 Day 1

# part one

def part_one():
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
    return(password)

# part two

def part_two():
    password = 0
    num = 50 
    with open("input", "r") as file:
        for line in file:
            turn = line.strip()
            direction = turn[0]
            m = int(turn[1:]) 
            if direction == 'R':
                start = num
                end = num + m
                password += end // 100 - start // 100
                num = end % 100

            else: 
                start = 99 - num
                end = 99 - (num - m)
                password += end // 100 - start // 100
                num = (num - m) % 100

    return(password)
