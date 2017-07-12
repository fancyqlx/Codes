class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor = 5
        result = 0
        while n != 0:
            result += n/factor
            n = n/factor
        return result
