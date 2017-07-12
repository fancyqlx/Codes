class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        array = []
        i = 0
        while i < len(nums):
            p = i + 1
            q = len(nums)-1
            while p < q:
                sum = - nums[p] - nums[q]
                if sum > nums[i]:
                    p += 1
                elif sum < nums[i]:
                    q -= 1
                else:
                    array.append([nums[i],nums[p],nums[q]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p-1]: p += 1
                    while p < q and nums[q] == nums[q+1]: q -= 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]: i += 1
        return array

