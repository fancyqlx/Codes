# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        return self.binarySearch(lower, upper)

    def binarySearch(self, lower, upper):
        mid = (upper + lower)/2
        if isBadVersion(mid):
            if mid-1 <= 0 or isBadVersion(mid-1) == False:
                return mid
            return self.binarySearch(lower, mid)
        else:
            return self.binarySearch(mid+1, upper)
