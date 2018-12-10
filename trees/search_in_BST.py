#https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from helpers.create_bst import insertIntoBST , TreeNode
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        root_val = root.val
        if root_val == val:
            return root
        if val > root_val:
                return self.searchBST(root.right, val)

        if val <= root_val:
                return self.searchBST(root.left, val)

    def iterative_approach(self, root, val):

        curr = root

        while True:
            if curr is None or curr.val == val:
                return curr
            elif curr.val <= val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left


test_root = TreeNode(1)
for i in range(10):
    insertIntoBST(test_root,i)


s = Solution()
b=s.iterative_approach(test_root, 5)
