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
        x = 0
        y = 0
        z = 0
        p = headA
        while p != None:
            p = p.next
            x += 1
        q = headB
        if q != None:
            p = q.next
            q.next = None
            y += 1
        while p != None:
            pre = q
            q = p
            p = p.next
            q.next = pre
            y += 1
        p = headA
        flag = 0
        while p != None:
            if p == headB:
                flag = 1
            p = p.next
            z += 1
        z -= 1
        intersec = (x+y-z)/2
        if q != None:
            p = q.next
            q.next = None
            intersec -= 1
        result = None
        if intersec == 0:
            result = q
        while p != None:
            pre = q
            q = p
            p = p.next
            q.next = pre
            intersec -= 1
            if intersec == 0:
                result = q
        if x == 0 or y == 0 or flag == 0:
            return None
        else:
            return result



