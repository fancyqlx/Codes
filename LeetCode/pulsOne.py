class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        if i < 0:
            return [1]
        digits[i] = digits[i] + 1
        if digits[i] <= 9:
            return digits
        digits[i] = 0
        carry = 1
        i = i - 1
        while i >= 0:
            digits[i] = digits[i] + carry
            if digits[i] > 9:
                digits[i] = 0
                carry = 1
                i = i - 1
                continue
            carry = 0
            break
        if carry == 1:
            digits.insert(0,1)
        return digits
