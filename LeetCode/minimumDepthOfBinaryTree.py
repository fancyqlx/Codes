# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        depth_l = 2147483647
        depth_r = 2147483647
        if root.left != None:
            depth_l = self.minimumDepth(root.left, 2)
        if root.right != None:
            depth_r = self.minimumDepth(root.right, 2)
        return min(depth_l,depth_r)


    def minimumDepth(self, root, depth):
        if root.left == None and root.right == None:
            return depth
        depth_l = 2147483647
        depth_r = 2147483647
        if root.left != None:
            depth_l = self.minimumDepth(root.left, depth+1)
        if root.right != None:
            depth_r = self.minimumDepth(root.right, depth+1)
        return min(depth_l,depth_r)
