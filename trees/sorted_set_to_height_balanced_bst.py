#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if nums:
            size = len(nums)
            if size == 1:
                root = TreeNode(nums[0])
                return root
            else:
                mid = size//2
                root = TreeNode(nums[mid])
                root.left=self.sortedArrayToBST(nums[:mid])
                root.right = self.sortedArrayToBST(nums[mid+1:])
                return root






s = Solution()
a = [-10,-3,0,5,9]
b = [-3,0]
s.sortedArrayToBST(a)

