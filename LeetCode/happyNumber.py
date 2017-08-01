class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = {}
        while n != 1:
            if table.has_key(n):
                return False
            else:
                table[n] = True
            n = self.SumOfSqures(n)
        return True


    def SumOfSqures(self, n):
        r = 0
        while n != 0:
            r += pow(n%10,2)
            n = n/10
        return r
