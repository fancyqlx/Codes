class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        T = {}
        for i in xrange(len(p)):
            if T.has_key(p[i]):
                T[p[i]][0] += 1
            else:
                T[p[i]] = [1,0]
        length = len(p)
        i = 0
        j = 0
        ans = []
        while j < len(s):
            if T.has_key(s[j]):
                T[s[j]][1] += 1
                if T[s[j]][0] >= T[s[j]][1]:
                    j += 1
                else:
                    while s[i] != s[j]:
                        T[s[i]][1] -= 1
                        i += 1
                    T[s[i]][1] -= 1
                    i += 1
                    j += 1
            else:
                while i != j:
                    T[s[i]][1] -= 1
                    i += 1
                j += 1
                i = j
            if j - i == length:
                ans.append(i)
        return ans

