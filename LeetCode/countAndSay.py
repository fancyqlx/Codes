class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 0:
            return ""
        pre = "1"
        for i in range(n-1):
            cur = ""
            count = 0
            position = pre[0]
            for j in range(len(pre)+1):
                if j<len(pre) and pre[j] == position:
                    count += 1
                    continue
                cur = cur + str(count) + position
                count = 1
                if j < len(pre):
                    position = pre[j]
            pre = cur
        return pre
