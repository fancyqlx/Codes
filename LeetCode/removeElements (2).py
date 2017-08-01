class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        count = 0
        i = 0
        while i < length:
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            i += 1
        return count
