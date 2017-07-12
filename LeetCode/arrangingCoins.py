class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while n >= i + 1 and n > 0:
            i += 1
            n -= i
        return i
