class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        T = {}
        for i in xrange(len(nums)):
            if T.has_key(nums[i]):
                if i-T[nums[i]]<=k:
                    return True
                else:
                    T[nums[i]] = i
            else:
                T[nums[i]] = i
        return False
