class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length1 = len(haystack)
        length2 = len(needle)
        if (length1-length2)<0:
            return -1
        elif length1 == 0 and length2 == 0:
            return 0
        i = 0
        while i < length1:
            if haystack[i:i+length2] == needle:
                return i
            i += 1
        return -1
