class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        max = 0
        a = 0
        for i in xrange(n):
            max += i * A[i]
            a += A[i]
        b = max
        for i in xrange(1, n):
            c = b + a  - n * A[n-i]
            if max < c:
                max = c
            b = c
        return max
