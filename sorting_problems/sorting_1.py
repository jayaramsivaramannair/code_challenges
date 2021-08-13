'''

Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Example:

prices = [1,2,3,4]
k = 7

The budget is 7 units of currency. He can buy items that cost [1,2,3] for 6 or [3,4] for 7 units. The maximum is 3 items.


Function Description:

Complete the function maximumToys in the editor below.

maximumToys has the following parameters:
- int prices[n]: the toy prices
- int k: Mark's Budget

Returns:

- int: the maximum number of toys

source: hackerrank.com (Interview Preparation on Sorting Problems)
'''

def maximumToys(prices, k):
    # Write your code here
    toys = 0
    amount_available = k
    prices.sort()
    for i in range(len(prices)):
        if prices[i] <= amount_available:
            toys += 1
            amount_available -= prices[i]
            
    return toys

print(maximumToys([1,12,5,111,200,1000,10], 50))