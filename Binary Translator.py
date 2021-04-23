#Binary Translator, (base 2 -> base 10), 23/04/2021
def convertToBin(bin):
    """This function converts decimal number
    to binary and prints it"""
    if bin > 1:
        convertToBin(bin // 2)
    print(bin % 2, end='')
while True:
    c = input("convert to binary (D) or convert to decimal (B): ")
    if c == "D":
        binary = input("input binary: ")
        num=0
        j=1
        i=0
        while i < len(binary):
            if binary[i] == "1":
                num+=j
            if binary[i] == "0":
                num*=2
            if binary[i] != "1" and binary[i] != "0":
                num="invalid input"
                break
            j*=2
            i+=1
        print(num)
    if c == "B":
        decimal = input("input decimal: ")
        convertToBin(int(decimal))
        print("\n")
    
