class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) != 0:
            for i in range(len(strs[0])):
                char = strs[0][i]
                for j in range(len(strs)):
                    if i >= len(strs[j]) or strs[j][i] != char:
                        return result
                result += char
        return result
