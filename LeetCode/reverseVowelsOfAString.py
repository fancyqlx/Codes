class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        i = 0
        j = len(l) - 1
        v = "aeiouAEIOU"
        while i < j:
            while i < j and (l[i] in v):
                if l[j] in v:
                    l[i],l[j] = l[j],l[i]
                    j -= 1
                    break
                j -= 1
            i += 1
        return "".join(l)
