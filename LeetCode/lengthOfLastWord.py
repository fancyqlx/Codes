class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0:
            if s[i].isalpha():
                j = i
                while i >= 0 and s[i].isalpha():
                    i = i - 1
                return j - i
            i -= 1
        return 0
