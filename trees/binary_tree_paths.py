#https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):

        if not root: return []
        if root.left is None and root.right is None: return [str(root.val)]
        s = '{}->'.format(root.val)
        out = []
        for i in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right):
            out.append(s+i)
        return out
