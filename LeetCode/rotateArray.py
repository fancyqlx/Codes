class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        temp = nums[:]
        for i in range(length):
            index = (i + k) % length
            nums[index] = temp[i]
