class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        T = {}
        flag = 0
        ans = 0
        for i in xrange(len(s)):
            if T.has_key(s[i]):
                T[s[i]] += 1
            else:
                T[s[i]] = 1
        for key in T:
            if T[key] % 2 == 1:
                ans += T[key] - 1
                flag = 1
            else:
                ans += T[key]
        if flag == 1:
            ans += 1
        return ans
