class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        c = (a & b) << 1 & mask
        r = (a ^ b) & mask
        while c != 0:
            r , c = (r ^ c) & mask, (r & c) << 1 & mask
        if (r>>31) == 1:
            r = ~(r ^ mask)
        return r
