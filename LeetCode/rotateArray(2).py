class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k%len(nums)-1)
        self.reverse(nums,k%len(nums),len(nums)-1)

    def reverse(self,nums,a,b):
        i = 0
        while i < (b-a+1)/2:
            temp = nums[a+i]
            nums[a+i] = nums[b-i]
            nums[b-i] = temp
            i += 1
