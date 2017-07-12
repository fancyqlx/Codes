class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        i = 0
        while i < 32:
            if n%2==1:
                result = result * 2 + 1
            else:
                result = result * 2
            n = n/2
            i = i + 1
        return result
