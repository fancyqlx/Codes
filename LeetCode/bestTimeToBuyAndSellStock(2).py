class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        index = 0
        profit = 0
        for i in range(len(prices)):
            if prices[index] < prices[i]:
                temp = prices[i] - prices[index]
                if temp > profit:
                    profit = temp
            else:
                index = i
        return profit
