# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        p = root.left
        q = root.right
        if p == None and q == None:
            return True
        elif p != None and q != None:
            pass
        else:
            return False
        pQueue = []
        qQueue = []
        pQueue.append(p)
        qQueue.append(q)
        while len(pQueue)!=0 and len(qQueue)!=0:
            if p.val != q.val:
                return False
            if p.left != None and q.right != None:
                pQueue.insert(0,p.left)
                qQueue.insert(0,q.right)
            elif p.left == None and q.right == None:
                pass
            else:
                return False
            if p.right != None and q.left != None:
                pQueue.insert(0,p.right)
                qQueue.insert(0,q.left)
            elif p.right == None and q.left == None:
                pass
            else:
                return False
            p = pQueue.pop()
            q = qQueue.pop()
        return True
