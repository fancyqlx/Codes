# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root == None:
            return ans
        if root.left != None:
            ans = self.Search(root.left, ans, 1)
        if root.right != None:
            ans = self.Search(root.right, ans, 0)
        return ans

    def Search(self, root, ans, flag):
        if root.left == None and root.right == None and flag == 1:
            return ans + root.val
        if root.left != None:
            ans = self.Search(root.left, ans, 1)
        if root.right != None:
            ans = self.Search(root.right, ans, 0)
        return ans
