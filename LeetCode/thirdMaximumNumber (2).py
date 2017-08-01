class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [-float('inf'),-float('inf'),-float('inf')]
        for i in xrange(len(nums)):
            for j in xrange(len(T)):
                if nums[i] > T[j]:
                    T.insert(j,nums[i])
                    if len(T) > 3:
                        T.pop()
                    break
                elif nums[i] == T[j]:
                    break
        if T[2] == -float('inf'):
            return T[0]
        return T[-1]


