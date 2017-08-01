# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        mid = (lower + upper)/2
        flag = guess(mid)
        if flag == 0:
            return mid
        elif flag == -1:
            return self.BinarySearch(lower,mid)
        else:
            return self.BinarySearch(mid+1,upper)

    def BinarySearch(self, lower, upper):
        mid = (lower + upper)/2
        flag = guess(mid)
        if flag == 0:
            return mid
        elif flag == -1:
            return self.BinarySearch(lower,mid)
        else:
            return self.BinarySearch(mid+1,upper)
