# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next
        p = head
        while p != None:
            q = p
            q = q.next
            while q != None and q.val == val:
                q = q.next
            p.next = q
            p = q
        return head
