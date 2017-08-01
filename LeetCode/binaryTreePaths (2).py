# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):
        s = ""
        if root == None:
            return []
        s = s + str(root.val)
        r = []
        if root.left != None:
            r = self.DFS(root.left,s,r)
        if root.right != None:
            r = self.DFS(root.right,s,r)
        if root.left == None and root.right == None:
            r.append(s)
        return r

    def DFS(self, root, s, r):
        s = s + "->" + str(root.val)
        if root.left != None:
            r = self.DFS(root.left,s,r)
        if root.right != None:
            r = self.DFS(root.right,s,r)
        if root.left == None and root.right == None:
            r.append(s)
        return r
