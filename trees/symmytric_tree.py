#https://leetcode.com/problems/symmetric-tree/

class Solution:

    def is_mirror(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        r = (a.val == b.val) and self.is_mirror(a.left, b.right) and self.is_mirror(a.right, b.left)

        return r

    def isSymmetric(self, root):
        return self.is_mirror(root, root)