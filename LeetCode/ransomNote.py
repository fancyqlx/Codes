class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        T = {}
        for i in xrange(len(magazine)):
            if T.has_key(magazine[i]):
                T[magazine[i]] += 1
            else:
                T[magazine[i]] = 1
        for i in xrange(len(ransomNote)):
            if T.has_key(ransomNote[i]) and T[ransomNote[i]] > 0:
                T[ransomNote[i]] -= 1
            else:
                return False
        return True
