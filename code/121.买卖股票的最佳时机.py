
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    min_p = prices[0]

    for i in range(len(prices)):
        if prices[i] < min_p:
            min_p = prices[i]
        elif prices[i] - min_p > profit:
            profit = prices[i] - min_p

    return profit



prices = [7,1,5,3,6,4] # [7,1,5,3,6,4]  [7,6,4,3,1] [3,3,5,0,0,3,1,4]
r = maxProfit(prices)
print(r)