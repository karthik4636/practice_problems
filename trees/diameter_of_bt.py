
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from trees.sorted_set_to_height_balanced_bst import Solution as S

#https://leetcode.com/problems/diameter-of-binary-tree/
class Solution:
    max_distance = 0
    def helper_node_to_leaf(self, node):
        if node is None:
            return 0
        left_depth = self.helper_node_to_leaf(node.left)
        right_depth = self.helper_node_to_leaf(node.right)
        a=left_depth+right_depth
        if a > self.max_distance:
           self.max_distance= a
        return max(left_depth, right_depth) + 1

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.helper_node_to_leaf(root)
        print(self.max_distance)










s = S()
root=s.sortedArrayToBST([1,2,3,4,5])
p = Solution()
p.diameterOfBinaryTree(root)