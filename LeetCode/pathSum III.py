# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        ans = 0
        path = []
        if root == None:
            return ans
        path.append(root.val)
        if path[-1] == sum:
            ans += 1
        if root.left != None:
            ans = self.DFS(root.left, sum, ans, path[:])
        if root.right != None:
            ans = self.DFS(root.right, sum, ans, path[:])
        return ans

    def DFS(self, root, sum, ans, path):
        for i in xrange(len(path)):
            path[i] = path[i] + root.val
            if path[i] == sum:
                ans += 1
        path.append(root.val)
        if path[-1] == sum:
            ans += 1
        if root.left != None:
            ans = self.DFS(root.left, sum, ans, path[:])
        if root.right != None:
            ans = self.DFS(root.right, sum, ans, path[:])
        return ans
