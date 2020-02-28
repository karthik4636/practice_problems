#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from trees.sorted_set_to_height_balanced_bst import Solution as S

class Solution():
    def rangeSumBST(self, root, L, R, sum=0):
        if root is None:
            return 0
        print(root.val)
        if root.val >= L and  root.val <=R:
                sum += root.val + self.rangeSumBST(root.left, L, R, sum)+ self.rangeSumBST(root.right, L, R, sum)
        elif root.val > L and root.val > R:
            sum +=  self.rangeSumBST(root.left, L, R, sum)
        elif root.val < L and root.val < R:
            sum +=  self.rangeSumBST(root.right, L, R, sum)
        return sum



s = S()
root=s.sortedArrayToBST([1,2,3,4, 5])
p = Solution()
print(p.rangeSumBST(root,1,1))









