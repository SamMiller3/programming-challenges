#Time to Type a String, problem from leetcode
#https://leetcode.com/discuss/interview-question/356477
"""Input: keyboard = "abcdefghijklmnopqrstuvwxy", text = "cba" 
Output: 4
Explanation:
Initially your finger is at index 0. First you have to type 'c'. The time taken to type 'c' will be abs(2 - 0) = 2 because character 'c' is at index 2.
The second character is 'b' and your finger is now at index 2. The time taken to type 'b' will be abs(1 - 2) = 1 because character 'b' is at index 1.
The third character is 'a' and your finger is now at index 1. The time taken to type 'a' will be abs(0 - 1) = 1 because character 'a' is at index 0.
The total time will therefore be 2 + 1 + 1 = 4."""
keyboard = "abcdefghijklmnopqrztuvwxyz"
text = input("input text: ")
count = 0
index = 0
for i in range(len(text)):
    count+=abs(index - (keyboard.index(text[i])))
    print("your finger was at " + str(index) + " but moving to " + str({text[i]}) + " took " + str(abs(index - (keyboard.index(text[i])))))
    index = text.index(text[i])
print(count)
