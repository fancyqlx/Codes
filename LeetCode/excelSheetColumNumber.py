class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        factor = 26
        for i in s:
            result = result * factor + ord(i) - 65 + 1
        return result

