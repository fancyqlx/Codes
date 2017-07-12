# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p = head
        head = head.next
        p.next = None
        while head != None:
            q = head
            head = head.next
            q.next = p
            p = q
        return p
