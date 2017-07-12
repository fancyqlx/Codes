class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        s = {}
        g = {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if s.has_key(secret[i]):
                    s[secret[i]] += 1
                else:
                    s[secret[i]] = 1
                if g.has_key(guess[i]):
                    g[guess[i]] += 1
                else:
                    g[guess[i]] = 1
        for key in s:
            if g.has_key(key):
                B += min(s[key],g[key])
        return ""+str(A)+"A"+str(B)+"B"

