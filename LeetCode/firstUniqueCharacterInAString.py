class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        T = {}
        for i in xrange(len(s)):
            if T.has_key(s[i]):
                T[s[i]] = -1
            else:
                T[s[i]] = i
        r = len(s)
        for key in T:
            if T[key] > -1 and T[key] < r:
                r = T[key]
        if r < len(s):
            return r
        return -1
