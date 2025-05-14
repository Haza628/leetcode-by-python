
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    last_p = prices[0]


    for i in range(len(prices)):

        if prices[i] - last_p > 0:
            profit += prices[i] - last_p
        last_p = prices[i]

    return profit

prices = [3,3,5,0,0,3,1,4] # [7,1,5,3,6,4]  [7,6,4,3,1] [3,3,5,0,0,3,1,4]
r = maxProfit(prices)
print(r)