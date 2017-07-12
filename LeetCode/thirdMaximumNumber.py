class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = []
        for i in xrange(len(nums)):
            flag = 0
            for j in xrange(len(T)):
                if nums[i] > T[j]:
                    T.insert(j,nums[i])
                    flag = 1
                    break
                elif nums[i] == T[j]:
                    flag = 1
                    break
            if len(T) > 3:
                T.pop()
            elif len(T) < 3 and flag == 0:
                T.append(nums[i])
        if len(T) == 3:
            return T[-1]
        elif len(T) > 0:
            return T[0]
        return -float('inf')


