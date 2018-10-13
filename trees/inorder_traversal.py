#refer: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)




root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)




inorder(root)








