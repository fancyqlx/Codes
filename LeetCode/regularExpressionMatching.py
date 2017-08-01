class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = 0
        length = len(p)
        for i in xrange(len(p)):
            if p[i] != '*': len_p += 1
        A = [[0 for j in xrange(len_p+1)] for i in xrange(len(s)+1)]
        A[0][0] = 1
        i = 0
        while i < len_s+1:
            k = 0
            j = 1
            while j < len_p+1 and k < length:
                if i == 0:
                    if k+1 < length and p[k+1] == '*' and A[0][j-1]:
                        A[0][j] = 1
                        k += 2
                    elif p[k] == '*': return False
                elif k+1 < length and p[k+1] == '*':
                    if (s[i-1] == p[k] or p[k] == '.') and (A[i-1][j-1] or A[i-1][j] or A[i][j-1]): A[i][j] = 1
                    elif s[i-1] != p[k] and p[k] != '.' and A[i][j-1]: A[i][j] = 1
                    k += 2
                elif (s[i-1] == p[k] or p[k] == '.') and A[i-1][j-1]:
                    A[i][j] = 1
                    k += 1
                elif p[k] == '*': return False
                else: k += 1
                j += 1
            if k < length and p[k]=='*': return False
            i += 1
        if A[len_s][len_p] == 1:
            return True
        return False
