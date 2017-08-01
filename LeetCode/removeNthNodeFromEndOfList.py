# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        x = head
        while x != None:
            length += 1
            x = x.next
        if length-n == 0:
            return head.next
        count = 0
        x = head
        while count < length-n-1:
            count += 1
            x = x.next
        y = x.next
        if y != None:
            x.next = y.next
        return head
