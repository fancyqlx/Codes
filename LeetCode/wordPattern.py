class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern == "":
            return False
        dic_s = {}
        str_s = ""
        list_s = str.split()
        if len(list_s) == 0 and len(str) > 0:
            if len(pattern) == 1:
                 return True
        if len(list_s) == len(pattern):
            num = 49
            for i in xrange(len(list_s)):
                if dic_s.has_key(list_s[i]):
                    str_s += dic_s[list_s[i]]
                else:
                    dic_s[list_s[i]] = chr(num)
                    str_s += dic_s[list_s[i]]
                    num += 1
            dic_p = {}
            str_p = ""
            num = 49
            for i in xrange(len(pattern)):
                if dic_p.has_key(pattern[i]):
                    str_p += dic_p[pattern[i]]
                else:
                    dic_p[pattern[i]] = chr(num)
                    str_p += dic_p[pattern[i]]
                    num += 1
            if str_s == str_p:
                return True
        return False
