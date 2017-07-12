# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        stack = []
        stack.append([0,root])
        result = 0
        while len(stack)>0:
            p = stack[-1][1]
            stack[-1][0] = 1
            result += p.val
            if p.right != None:
                stack.append([0,p.right])
            if p.left != None:
                stack.append([0,p.left])
            if p.right == None and p.left == None:
                if result == sum:
                    return True
                while len(stack)>0 and stack[-1][0] == 1:
                    p = stack.pop()[1]
                    result -= p.val
        return False
