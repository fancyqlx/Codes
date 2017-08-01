class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        T = {}
        for i in xrange(len(s)):
            if T.has_key(s[i]):
                T[s[i]] += 1
            else:
                T[s[i]] = 1
        for i in xrange(len(t)):
            if T.has_key(t[i]):
                T[t[i]] -= 1
            else:
                return t[i]
        for key in T:
            if T[key] < 0:
                return key
        return t[-1]
