# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p = head
        q = p.next
        while q != None:
            if q.val == p.val:
                p.next = q.next
                q = q.next
                continue
            p.next = q
            p = q
            q = q.next
        return head
