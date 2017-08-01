class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        temp_nums = []
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
                temp_nums.append(nums[i])
            elif dic[nums[i]] < 3:
                dic[nums[i]] += 1
                temp_nums.append(nums[i])
        dic = {}
        dic_f = {}
        array = []
        nums = temp_nums
        nums.sort()
        for i in xrange(len(nums)):
            dic[nums[i]] = i
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                k = -nums[i] - nums[j]
                if (k in dic) and (dic[k] > j) and (nums[i],nums[j]) not in dic_f:
                    array.append([nums[i],nums[j],k])
                    dic_f[(nums[i],nums[j])] = k
        return array

