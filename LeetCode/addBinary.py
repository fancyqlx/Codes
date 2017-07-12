class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = ""
        i = len(a) - 1
        j = len(b) - 1
        y = ""
        for k in range(abs(i-j)):
            y = y + '0'
        if i < j:
            a = y + a
            i = j
        else:
            b = y + b
        carry = 0
        while i>=0:
            if carry == 1:
                if a[i] == '1' and b[i] == '1':
                    x = x + '1'
                    carry = 1
                elif a[i] == '0' and b[i] == '0':
                    x = x + '1'
                    carry = 0
                else:
                    x = x + '0'
                    carry = 1
            else:
                if a[i] == '1' and b[i] == '1':
                    x = x + '0'
                    carry = 1
                elif a[i] == '0' and b[i] == '0':
                    x = x + '0'
                    carry = 0
                else:
                    x = x + '1'
                    carry = 0
            i = i - 1
        if carry == 1:
            x = x + '1'
        y = ""
        k = len(x) - 1
        while k >= 0:
            y = y + x[k]
            k = k - 1
        return y


