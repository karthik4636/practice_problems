
# A preorder traversal of a binary tree will
# always begin with the root element,
# and continue in a DFS-style manner.
# This means that we can pop elements off of
# the preorder list to obtain the next element
# of the tree. Finding the index of that
# element in the inorder list allows us to
# determine what elements are on the left/right
# branches of that element. We then recursively
# run through the left and right subtrees,
# passing only the elements on the left to the left,
# and only the elements on the right to the right.
# Popping off the list means that the preorder traversal
# will always be in the correct order.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        partition = inorder.index(root.val)

        root.left = self.buildTree(preorder,inorder[0:partition])
        root.right = self.buildTree(preorder,inorder[partition+1:])
        return root
s = Solution()
s.buildTree(preorder = [3,9,20,15,7]
,inorder = [9,3,15,20,7])