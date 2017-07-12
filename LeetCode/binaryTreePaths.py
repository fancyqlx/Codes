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
        l = []
        r = []
        if root.left != None:
            l = self.DFS(root.left,s)
        if root.right != None:
            r = self.DFS(root.right,s)
        if l != [] or r != []:
            return l + r
        r.append(s)
        return r

    def DFS(self, root, s):
        s = s + "->" + str(root.val)
        l = []
        r = []
        if root.left != None:
            l = self.DFS(root.left,s)
        if root.right != None:
            r = self.DFS(root.right,s)
        if l != [] or r != []:
            return l + r
        r.append(s)
        return r
