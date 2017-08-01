class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        for i in xrange(len(num1)-len(num2)):
            num2 = '0' + num2
        for i in xrange(len(num2)-len(num1)):
            num1 = '0' + num1
        c = 0
        ans = ""
        for i in xrange(len(num1)-1,-1,-1):
            a = ord(num1[i])-48
            b = ord(num2[i])-48
            ans = str((a + b + c) % 10) + ans
            if a + b + c > 9:
                c = 1
            else:
                c = 0
        if c == 1:
            ans = '1' + ans
        return ans
