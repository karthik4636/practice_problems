#https://leetcode.com/problems/invert-binary-tree/
from helpers.create_bst import insertIntoBST, TreeNode

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        stack= []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur.left, cur.right = cur.right, cur.left
                cur = cur.left


test_root = TreeNode(1)
for i in range(3):
    if i!=1:
        insertIntoBST(test_root,i)


s = Solution()
b=s.invertTree(test_root)
