# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        p = head
        while p != None:
            p = p.next
            length = length + 1
        p = head
        q = head
        if p != None:
            q = p.next
            p.next = None
        for i in xrange(length/2-1):
            temp = q
            q = q.next
            temp.next = p
            p = temp
        if length%2!=0 and q != None:
            q = q.next
        while p != None and q != None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
