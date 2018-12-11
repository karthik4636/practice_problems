#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from helpers.create_bst import insertIntoBST, TreeNode


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val <= q.val:
            p, q = q, p
        while True:
            if root is p or root is q:
                return root
            elif root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root


test_root = TreeNode(5)
for i in range(10):
    insertIntoBST(test_root, i)

s = Solution()
p = test_root.left
q = test_root.right
s.lowestCommonAncestor(test_root, p, q)
