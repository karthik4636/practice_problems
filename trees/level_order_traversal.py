# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from helpers.create_bst import insertIntoBST, TreeNode


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tmp = [root]
        result = []
        c = [root.val]
        while tmp:
            result.append(c)
            b = []
            c = []
            for i in tmp:
                if i.left:
                    b.append(i.left)
                    c.append(i.left.val)
                if i.right:
                    b.append(i.right)
                    c.append(i.right.val)
            tmp = b
        return result


test_root = TreeNode(2)
for i in [1, 3]:
    insertIntoBST(test_root, i)

s = Solution()
s.levelOrder(test_root)
