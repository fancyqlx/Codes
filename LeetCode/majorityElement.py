class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dic = {}
        result = []
        for i in nums:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
            if dic[i] >= length/2:
                result.append((dic[i],i))
        result.sort(reverse=1)
        return result[0][1]
