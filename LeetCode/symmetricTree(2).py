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
        return self.recursion(root.left,root.right)

    def recursion(self, p, q):
        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.val == q.val:
                return self.recursion(p.left,q.right) & self.recursion(p.right,q.left)
            return False
        return False
