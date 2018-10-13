class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def min_depth(root):
    if root is None:
        return 0
    #leaf node
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return 1+min_depth(root.right)
    if root.right is None:
        return 1+min_depth(root.left)
    return 1+min(min_depth(root.left),min_depth(root.right))









root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)

print(min_depth(root))