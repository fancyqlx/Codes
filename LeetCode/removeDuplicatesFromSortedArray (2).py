class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        count = 1
        i = 1
        j = 1
        while i < length:
            if nums[i] != nums[i-1]:
                count += 1
                nums[j] = nums[i]
                j += 1
            i += 1
        return count
