class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        r = 0
        c = 0
        for i in xrange(32):
            r = r | ((a ^ b) & (1 << i) ^ c)
            if a & b & (1 << i):
                c = a & b & (1 << i)
            else:
                c = (a ^ b) & c
            c = c << 1
        if (r>>31) == 1:
            r = ~(r ^ 0xffffffff)
        return r