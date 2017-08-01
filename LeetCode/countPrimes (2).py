"""
range() function produces a list, which needs too much memeory.
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        nums = [1 for i in xrange(n)]
        nums[0] = 0
        nums[1] = 0
        i = 2
        while i * i < n:
            if nums[i] == 1:
                nums[i**2::i] = [0] * len(nums[i**2::i])
            i += 1
        count = 0
        for i in xrange(n):
            if nums[i] == 1:
                count += 1
        return count
