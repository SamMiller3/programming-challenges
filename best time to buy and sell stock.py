#Best time to buy and sell stock, 10/09/2022
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
#Find the maximum profit you can achieve. You may complete at most k transactions.
#Example:
#Input: k = 2, prices = [2,4,1]
#Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

#Variables:

prices=[3,2,6,5,0,3]
k=2
profitPerPurchase=[]
profit=0

#Main Code:

#iterate through list prices to find profit each stock
for i in range(len(prices)-1):
    #iterate through starting from each stock to find optimal place to sell
    for j in range(i+1,len(prices)):
        profitPerPurchase.append(prices[j]-prices[i])
#remove negative numbers
profitPerPurchase = [item for item in profitPerPurchase if item >= 0]
#sort in ascending order
profitPerPurchase.sort(reverse = True)
#purchase most profitable stocks
for i in range(len(profitPerPurchase)):
    if i>=k:
        break
    profit+=profitPerPurchase[i]
#output profit
print(profit)
