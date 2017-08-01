# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p != None and p.next != None:
            t = p.next.val
            p.next.val = p.val
            p.val = t
            p = p.next.next
        return head