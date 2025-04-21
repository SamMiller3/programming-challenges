# Problem: Minimum Window Substring
# Date: 22/10/2022
# Given strings s and t, return the smallest window in s that contains all characters of t.
# If no such window exists, return an empty string.

s = "ADOBECODEBANC"
t = "ABC"
all_substrings = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substr = s[i:j]
        temp_t = list(t)

        for ch in substr:
            if ch in temp_t:
                temp_t.remove(ch)

        if not temp_t:  # all chars from t found
            all_substrings.append(substr)
            break  # no need to check longer substrings from this i

# Output shortest valid substring
if all_substrings:
    print(min(all_substrings, key=len))
else:
    print("")
