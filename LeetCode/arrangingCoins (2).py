class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = int((pow(8*n+1,0.5)-1)/2)
        while n - (i+1)*i/2 > i:
            i += 1
        return i
