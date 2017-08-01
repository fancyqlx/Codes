# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        r = l1
        carry = 0
        while p != None and q != None:
            p.val = p.val + q.val + carry
            if p.val > 9:
                carry = 1
            else:
                carry = 0
            p.val %= 10
            q.val = p.val
            r = p
            p = p.next
            q = q.next
        if p == None and q == None and carry == 1:
            r.next = ListNode(1)
            return l1
        if p != None:
            while p != None and carry == 1:
                p.val = p.val + carry
                if p.val > 9:
                    carry = 1
                else:
                    carry = 0
                p.val %= 10
                r = p
                p = p.next
            if carry == 1:
                r.next = ListNode(1)
            return l1

        while q != None and carry == 1:
            q.val = q.val + carry
            if q.val > 9:
                carry = 1
            else:
                carry = 0
            q.val %= 10
            r = q
            q = q.next
        if carry == 1:
            r.next = ListNode(1)
        return l2

