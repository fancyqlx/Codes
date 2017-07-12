# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        while p != q:
            if p != None:
                p = p.next
            else:
                p = headB
            if q != None:
                q = q.next
            else:
                q = headA
        return p



