#https://leetcode.com/problems/validate-binary-search-tree/

class Solution(object):

    def is_valid_helper(self, root, min, max):
        if root is None:
            return True

        if root.val <= min or root.val >= max:
            return False

        return self.is_valid_helper(root.left, min, root.val) and \
               self.is_valid_helper(
                   root.right, root.val, max)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid_helper(root, float("-inf"), float("inf"))
