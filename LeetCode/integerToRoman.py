class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        factor = 10
        s = ""
        while num != 0:
            target = (num % factor)/(factor/10)
            num = num - num % factor
            while target <= 3 and target > 0:
                s = dic[factor/10] + s
                target -= 1
            if target == 4:
                s = dic[factor/10] + dic[factor/2] + s
            elif target == 9:
                s = dic[factor/10] + dic[factor] + s
            elif target >= 5:
                temp = dic[factor/2]
                while target > 5:
                    temp = temp + dic[factor/10]
                    target -= 1
                s = temp + s
            factor *= 10
        return s

