class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)>0:
            lower = 0
            upper = len(nums)-1
            if upper != lower:
                mid = (upper + lower)/2
                nums = self.divide(nums, lower, mid)
                nums = self.divide(nums, mid + 1, upper)
                nums = self.merge(nums, lower, upper)


    def divide(self, nums, lower, upper):
        if upper == lower:
            return nums
        mid = (upper + lower)/2
        nums = self.divide(nums, lower, mid)
        nums = self.divide(nums, mid + 1, upper)
        return self.merge(nums, lower, upper)


    def merge(self, nums, lower, upper):
        if upper == lower:
            return nums
        mid = (upper + lower)/2
        count = 0
        for i in xrange(lower, mid+1):
            if nums[i] == 0:
                count += 1
        i = count
        j = mid + 1
        while j <= upper and nums[j] != 0:
            nums[j - count] = nums[j]
            j += 1
        while i != 0:
            nums[j-i] = 0
            i -= 1
        return nums
