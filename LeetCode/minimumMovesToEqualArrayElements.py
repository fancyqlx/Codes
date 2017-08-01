class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        s = 0
        l = len(nums)
        if l >= 2:
            s = nums[l-1] - nums[0]
            ans += s
        for i in xrange(l-1, 0,-1):
            s = nums[i-1] - nums[i] + s
            ans += s
        return ans
