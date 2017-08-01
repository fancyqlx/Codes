class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0:
            return True
        i = 0
        j = length - 1
        while i<j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                        continue
                    else:
                        return False
                j -= 1
            else:
                i += 1
        return True

