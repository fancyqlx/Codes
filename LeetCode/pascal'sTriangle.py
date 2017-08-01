class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j-1 >= 0 and j <= i-1:
                    row.append(triangle[i-1][j-1]+triangle[i-1][j])
                else:
                    row.append(1)
            triangle.append(row)
        return triangle
