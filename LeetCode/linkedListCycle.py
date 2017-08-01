# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        pre = head
        p = head.next
        while p != None:
            if p == head:
                return True
            q = p
            p = p.next
            q.next = pre
            pre = q
        return False
