class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(s)):
            if dic.has_key(s[i]):
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        for i in xrange(len(t)):
            if dic.has_key(t[i]):
                dic[t[i]] -= 1
            else:
                return False
        for i in dic:
            if dic[i] != 0:
                return False
        return True

