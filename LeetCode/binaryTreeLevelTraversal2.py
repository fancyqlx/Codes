# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        r = []
        queue = []
        queue.append(root)
        c_level = 1
        while len(queue)>0:
            n_level = 0
            level = []
            while c_level>0:
                p = queue.pop()
                level.append(p.val)
                c_level -= 1
                if p.left != None:
                    queue.insert(0,p.left)
                    n_level += 1
                if p.right != None:
                    queue.insert(0,p.right)
                    n_level += 1
            r.insert(0,level)
            c_level = n_level
        return r




