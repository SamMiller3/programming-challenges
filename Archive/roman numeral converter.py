#convert from roman numerals to integers, date made: 21/03/22
while True:
    roman = input("input some roman numerals")
    e=0
    b=0
    rmns = list(roman)
    for i in range(len(roman)):
        if roman[i] == "I":
            rmns[i] = 1
        if roman[i] == "V":
            rmns[i] = 5
        if roman[i] == "X":
            rmns[i] = 10
        if roman[i] == "L":
            rmns[i] = 50
        if roman[i] == "C":
            rmns[i] = 100
        if roman[i] == "D":
            rmns[i] = 500
        if roman[i] == "M":
            rmns[i] = 1000
    for i in range(len(roman)):
        if roman[i] == "I":
            e+=1
        if roman[i] == "V":
            e+=5
        if roman[i] == "X":
            e+=10
        if roman[i] == "L":
            e+=50
        if roman[i] == "C":
            e+=100
        if roman[i] == "D":
            e+=500
        if roman[i] == "M":
            e+=1000
        if i != len(roman)-1:
            if rmns[i] != rmns[i+1]:
                if(rmns[i] < rmns[i+1]):
                    b-=e
                    e=0
                if (rmns[i] > rmns[i+1]):
                    b+=e
                    e=0
        if i == len(roman)-1:
            b+=e
    print(b)
