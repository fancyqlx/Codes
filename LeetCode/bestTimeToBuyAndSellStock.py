class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        buy = prices[0]
        min = prices[0]
        sell = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                profit = sell - buy
            elif prices[i] < min:
                min = prices[i]
            if prices[i] - min > profit:
                buy = min
                sell = prices[i]
                profit = sell - buy
        return profit
