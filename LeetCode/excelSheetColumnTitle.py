class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        factor = 26
        while n != 0:
            remainder = n%factor
            n = n/factor
            if remainder == 0:
                s += 'Z'
                n -= 1
            else:
                s += chr(remainder-1+65)
        result = ""
        for i in range(len(s)-1,-1,-1):
            result += s[i]
        return result
