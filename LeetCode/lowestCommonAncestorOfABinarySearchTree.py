# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        r = None
        c = 0
        if root == p:
            return p
        elif root == q:
            return q
        if root != None:
            c_1, r = self.recursion(root.left, p, q, r)
            c_2, r = self.recursion(root.right, p, q, r)
            c = c_1 + c_2
        if r == None and c == 2:
            r = root
        return r

    def recursion(self, root, p, q, r):
        c_0 = 0
        c_1 = 0
        c_2 = 0
        if root == p or root == q:
            c_0 = 1
        if root != None:
            c_1, r = self.recursion(root.left, p, q, r)
            c_2, r = self.recursion(root.right, p, q, r)
        c = c_0 + c_1 + c_2
        if r == None and c == 2:
            r = root
        return c, r
