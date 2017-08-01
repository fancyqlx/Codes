class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        i = 0
        sum = 0
        while sum < n:
            i += 1
            sum += i*(pow(10,i)-pow(10,i-1))
        sum -= i*(pow(10,i)-pow(10,i-1))
        i -= 1
        num = pow(10,i) + (n-sum-1)/(i+1)
        pos = i+1-(n-sum-1)%(i+1)
        return (num%pow(10,pos))/pow(10,pos-1)

