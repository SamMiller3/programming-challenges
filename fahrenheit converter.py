#celsius to fahrenheit (32°C × 9/5) + 32 = 89.6°F   (32°F − 32) × 5/9 = 0°C
while True:
    to = ""
    to = input("inputting celsius (c) or fahreneheit (f)?")
    inpt = int(input("input a number"))
    if to == "c":
        print ((inpt * 9/5) + 32)
    if to == "f":
        print ((inpt - 32) * 5/9)
