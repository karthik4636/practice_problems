class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def max_depth(root):
    if not root:
        return 0

    ldepth = max_depth(root.left)
    rdepth = max_depth(root.right)
    return max(ldepth, rdepth)+1








root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)

print(max_depth(root))