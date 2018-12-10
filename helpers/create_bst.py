class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertIntoBST( root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None:
        return TreeNode(5)

    root_val = root.val
    if val > root_val:
        if root.right is None:
            root.right = TreeNode(val)
        else:

            insertIntoBST(root.right, val)

    if val <= root_val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insertIntoBST(root.left, val)

    return root