class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        hash_1 = {}
        hash_2 = {}
        j = 0
        for i in xrange(length):
            if (not hash_1.has_key(s[i])) and (not hash_2.has_key(t[i])):
                j = j + 1
                hash_1[s[i]] = str(j)
                hash_2[t[i]] = str(j)
            elif hash_1.has_key(s[i]) and hash_2.has_key(t[i]):
                pass
            else:
                return False
            if hash_1[s[i]] != hash_2[t[i]]:
                return False
        return True
