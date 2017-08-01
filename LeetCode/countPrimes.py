class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        nums = [1] * n
        nums[0] = 0
        nums[1] = 0
        for i in xrange(2,int(n**0.5)+1):
            if nums[i] == 1:
                nums[i**2::i] = [0] * len(nums[i**2::i])
        return sum(nums)
