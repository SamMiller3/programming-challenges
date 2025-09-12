# 12/09/25
# Problem 31, Coin Sums

def dp(i,j):
    if j == 0:
        return 1
    if i == 0 or j<0:
        return 0
    return(dp(i-1,j)+dp(i, j-coins[i-1]))


coins = [1,2,5,10,20,50,100,200]
print(dp(8, 200))