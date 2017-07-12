# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        depth = 1
        depth_l = self.recursiveDepth(root.left, depth+1)
        depth_r = self.recursiveDepth(root.right, depth+1)
        if depth_l[0] == False or depth_r[0] == False:
            return False
        elif abs(depth_l[1]-depth_r[1])>1:
            return False
        else:
            return True

    def recursiveDepth(self, root, depth):
        if root == None:
            return (True, depth-1)
        depth_l = self.recursiveDepth(root.left, depth+1)
        depth_r = self.recursiveDepth(root.right, depth+1)
        if depth_l[0] == False or depth_r[0] == False:
            return (False, max(depth_l[1],depth_r[1]))
        elif abs(depth_l[1]-depth_r[1])>1:
            return (False, max(depth_l[1],depth_r[1]))
        else:
            return (True, max(depth_l[1],depth_r[1]))


