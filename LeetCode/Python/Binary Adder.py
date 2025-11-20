#Binary Adder, 14/07/2023
#Challenge from leetcode.com
#Given two binary strings a and b, return their sum as a binary string.


carryBit = 0
outBit = []
a = "101"
b = "1011"

#if one bit is longer than another, then concatenate 0s to the beginning so both bits are same length
if len(a) != len(b):
    shortBit = min((a, b), key=len)
    longBit = max((a, b), key=len)
    shortBit = "0" * (len(longBit) - len(shortBit)) + shortBit
    a, b = shortBit, longBit

#iterate thru, and calculate the sum of current index of a and b
#if its 2 or more set the carry bit to true, and add carrybit to sum
#each time, otherwise set carrybit to false.
for i in range(len(a)-1, -1, -1):
    bitSum = int(a[i]) + int(b[i]) + carryBit
    outBit.insert(0, str(bitSum % 2))
    carryBit = bitSum // 2

if carryBit == 1:
    outBit.insert(0, "1")

print(''.join(outBit))
