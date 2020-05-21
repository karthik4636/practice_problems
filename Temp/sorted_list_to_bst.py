#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        curr = head
        numArray = []
        while curr is not None:
            numArray.append(curr.val)
            curr = curr.next
        return self.sortedArrayToBst(numArray)

    def sortedArrayToBst(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2

        root = TreeNode(arr[mid])

        root.left = self.sortedArrayToBst(arr[:mid])
        root.right = self.sortedArrayToBst(arr[mid + 1:])

        return root