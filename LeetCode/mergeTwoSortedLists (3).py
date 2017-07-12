# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        elif l2==None:
            return l1
        if l1.val<=l2.val:
            p = l1
            q = l2
        else:
            p = l2
            q = l1
        l = p
        while p.next != None:
            if p.next.val > q.val:
                t = p.next
                p.next = q
                p = q
                q = t
            else:
                p = p.next
        p.next = q
        return l
