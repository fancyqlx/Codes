class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i = 0
        j = len(height)-1
        if j < 1:
            return None
        while i < j:
            while height[i]<=height[j] and i<j:
                temp = (j-i)*height[i]
                if temp >= area:
                    area = temp
                i += 1
            while height[i]>height[j] and i<j:
                temp = (j-i)*height[j]
                if temp >=area:
                    area = temp
                j -= 1
        return area
