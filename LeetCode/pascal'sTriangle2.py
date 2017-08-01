class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [1]
        b = []
        for i in range(rowIndex+1):
            for j in range(i+1):
                if i-1 >= 0 and j-1 >= 0 and j < i:
                    b.append(a[j-1]+a[j])
                else:
                    b.append(1)
            a = b
            b = []
        return a
