'''
    This method takes O(n1+n2) but it needs too many operations.
'''
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
        ex = min(l1.val,l2.val)
        p = ListNode(None)
        l = p
        while l1!=None or l2!=None:
            while l1!=None and l1.val<=ex:
                q = ListNode(None)
                q.val = l1.val
                q.next = None
                p.next = q
                p = q
                l1 = l1.next
            if l1!=None:
                ex = l1.val
            else:
                p.next = l2
            while l2!=None and l2.val<=ex:
                q = ListNode(None)
                q.val = l2.val
                q.next = None
                p.next = q
                p = q
                l2 = l2.next
            if l2!=None:
                ex = l2.val
            else:
                p.next = l1
        l = l.next
        return l
