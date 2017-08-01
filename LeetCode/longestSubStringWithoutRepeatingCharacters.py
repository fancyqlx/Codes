class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        T = {}
        ans = 0
        l = 0
        while j < len(s):
            if T.has_key(s[j]) and T[s[j]] == 1:
                while s[i] != s[j]:
                    T[s[i]] = 0
                    i += 1
                if l >= ans:
                    ans = l
                l = j - i
                i += 1
                j += 1
            else:
                T[s[j]] = 1
                l += 1
                j += 1
        if l >= ans:
            ans = l
        return ans

