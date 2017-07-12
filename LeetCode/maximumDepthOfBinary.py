# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.countLength(2,root.left),self.countLength(2,root.right))

    def countLength(self,length,root):
        if root == None:
            return length-1
        return max(self.countLength(length+1,root.left),self.countLength(length+1,root.right))

