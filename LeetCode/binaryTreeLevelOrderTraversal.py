# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        r = []
        if root == None:
            return r
        queue = []
        queue.append(root)
        m = 1
        n = 0
        while len(queue) > 0:
            subR = []
            while m != 0:
                p = queue.pop()
                subR.append(p.val)
                m -= 1
                if p.left != None:
                    queue.insert(0,p.left)
                    n += 1
                if p.right != None:
                    queue.insert(0,p.right)
                    n += 1
            r.append(subR)
            m = n
            n = 0
        return r



