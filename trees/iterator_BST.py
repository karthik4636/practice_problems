#https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from helpers.create_bst import insertIntoBST, TreeNode

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.current = None
        self.stack = []
        self.generator = self.gen(root)
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack or (self.current is not self.last))

    def next(self):
        for i in self.generator:

            return i


    def gen(self, root):
        """
        :rtype: int
        """
        self.current = root
        while self.current or self.stack:
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            else:
                self.current = self.stack.pop()
                yield self.current.val
                self.current = self.current.right


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())



test_root = TreeNode(5)
for i in range(10):
    insertIntoBST(test_root, i)


i = BSTIterator(root= test_root)

i, v = BSTIterator(test_root), []

# g = i.gen()
# for j in g:
#      print(j)


while i.hasNext():
    print(i.next())