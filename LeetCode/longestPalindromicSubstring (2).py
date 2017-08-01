class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        t = ""
        for i in xrange(len(s)):
            t += "#" + s[i]
        t += "#"
        c = 0
        r = 0
        p = [0 for i in xrange(len(t))]
        max_index = 0
        n = len(t)
        for i in xrange(n):
            i_mirror = 2*c - i
            if r > i:
                p[i] = min(p[i_mirror],r-i)
            else:
                p[i] = 0
            while i-p[i]-1 >= 0 and i+p[i]+1 < n and t[i+p[i]+1] == t[i-p[i]-1]:
                p[i] += 1
            if p[i] >= p[max_index]:
                max_index = i
            if i+p[i]>r:
                c = i
                r = i + p[i]
        return s[(max_index-p[max_index])/2 : (max_index+p[max_index])/2]
