# 13/11/2023 2147. Number of Ways to Divide a Long Corridor
# Problem: Count the number of ways to divide a corridor into sections with exactly 2 seats ('S') each.
# Constraints: Sections must be separated by any number of plants ('P'), modulo 10^9 + 7.

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        zero = 0
        one = 0
        two = 1

        for thing in corridor:
            if thing == 'S':
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        return zero
