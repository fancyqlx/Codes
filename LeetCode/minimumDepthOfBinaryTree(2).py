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
        queue = []
        queue.append(root)
        depth = 1
        count = 1
        while len(queue)>0:
            newCount = 0
            while count>0:
                p = queue.pop()
                count -= 1
                if p.left != None:
                    queue.insert(0,p.left)
                    newCount += 1
                if p.right != None:
                    queue.insert(0,p.right)
                    newCount += 1
                if p.left == None and p.right == None:
                    return depth
            depth += 1
            count = newCount

