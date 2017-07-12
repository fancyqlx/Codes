class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length > 1:
            nums[1] = max(nums[0],nums[1])
        for i in range(2,length):
            nums[i] = max(nums[i-2]+nums[i],nums[i-1])
        return nums[length-1]



