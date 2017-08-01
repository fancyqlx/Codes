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
        k_1=""
        k_2=""
        j = 1
        for i in xrange(length):
            if hash_1.has_key(s[i]) and hash_2.has_key(t[i]):
                k_1 += hash_1[s[i]]
                k_2 += hash_2[t[i]]
            elif (not hash_1.has_key(s[i])) and (not hash_2.has_key(t[i])):
                j = j + 1
                hash_1[s[i]] = str(j)
                hash_2[t[i]] = str(j)
                k_1 += hash_1[s[i]]
                k_2 += hash_2[t[i]]
            else:
                return False
        if k_1 == k_2:
            return True
        return False
