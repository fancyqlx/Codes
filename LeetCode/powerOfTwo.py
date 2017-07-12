class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        flag = 0
        while n != 0:
            if n%2==1:
                if flag == 1:
                    return False
                else:
                    flag = 1
            n=n>>1
        return True
