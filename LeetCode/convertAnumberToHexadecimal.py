class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        mask = 0xffffffff
        mask_l = 0x0000000f
        T = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        ans = ""
        num = num & mask
        if num == 0:
            return '0'
        while num != 0:
            ans = T[num & mask_l] + ans
            num = num >> 4 & mask
        return ans
