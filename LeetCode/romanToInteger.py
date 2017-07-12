class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)):
            result += dic[s[i]]
            if i-1 >= 0 and dic[s[i-1]] < dic[s[i]]:
                result = result - dic[s[i-1]] - dic[s[i-1]]
        return result
