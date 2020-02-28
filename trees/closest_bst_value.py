#https://leetcode.com/problems/closest-binary-search-tree-value/
from math import floor, ceil
from trees.sorted_set_to_height_balanced_bst import Solution as S

class Solution:
    closestV = float("inf")

    def closestValue(self, root , target):
        if root is None:
            return
        if abs(self.closestV-target) > abs(root.val-target):
            self.closestV = root.val
        if target > root.val:
               self.closestValue(root.right, target)
        else:
               self.closestValue(root.left, target)

        return self.closestV





s = S()
root=s.sortedArrayToBST([1,2,3,4,5,6])
p = Solution()
print(p.closestValue(root,5.1))


