class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        T = {}
        for i in xrange(len(nums)):
            if T.has_key(nums[i]):
                return True
            T[nums[i]] = True
        return False
