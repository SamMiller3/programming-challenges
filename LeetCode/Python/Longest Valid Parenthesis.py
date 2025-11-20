# Problem: Longest Valid Parentheses
# Date: 05/02/2023
# Given a string s containing only '(' and ')', return the length of the longest
# well-formed (balanced) parentheses substring.

s = ")("
max_length = 0
stack = [-1]  # stores index of last unmatched ')'

for i, char in enumerate(s):
    if char == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            max_length = max(max_length, i - stack[-1])

print(max_length)  # Output: 0
