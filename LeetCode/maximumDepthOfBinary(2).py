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
        stack = []
        stack.append((1,root))
        length = 1
        while len(stack) > 0:
            pebble = stack[-1][0]
            p = stack[-1][1]
            stack.pop()
            if p.left == None and p.right == None:
                length = max(pebble,length)
                continue
            if p.left != None:
                stack.append((pebble+1,p.left))
            if p.right != None:
                stack.append((pebble+1,p.right))
        return length

