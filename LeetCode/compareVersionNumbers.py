class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        la = []
        lb = []
        a = ""
        b = ""
        for i in version1:
            if i == '.':
                la.append(int(a))
                a = ""
                continue
            a += i
        la.append(int(a))
        for j in version2:
            if j == '.':
                lb.append(int(b))
                b = ""
                continue
            b += j
        lb.append(int(b))
        length1 = len(la)
        length2 = len(lb)
        length = 0
        if length1-length2>0:
            length = length1
            for i in range(length1-length2):
                lb.append(0)
        else:
            length = length2
            for i in range(length2-length1):
                la.append(0)
        for i in range(length):
            if la[i] > lb[i]:
                return 1
            elif la[i] < lb[i]:
                return -1
        return 0
