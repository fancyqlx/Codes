class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        T = [[i] for i in xrange(len(s))]
        max_index = 0
        min_index = 0
        max_len = 0
        for i in xrange(1,len(s)):
            if s[i] == s[i-1]:
                T[i].append(i-1)
            for x in T[i-1]:
                if x-1 >= 0 and s[i] == s[x-1]:
                    T[i].append(x-1)
            if i - T[i][-1] + 1 >= max_len:
                max_index = i
                min_index = T[i][-1]
                max_len = max_index - min_index + 1
        if max_len > 0:
            return s[min_index:max_index+1]
        return s[-1]
