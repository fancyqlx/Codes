'''
    It is faster but the pointer operations are not concise enough.
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
        if l1.val<=l2.val:
            p = l1
            q = l2
        else:
            p = l2
            q = l1
        l = p
        pPre = p
        qPre = None
        while p!=None and q!=None:
            if q.val<p.val:
                pPre.next = q
                while q!= None and q.val<p.val:
                    qPre = q
                    q = q.next
                qPre.next = p
            pPre = p
            p = p.next
        if q!=None:
            pPre.next = q
        return l
