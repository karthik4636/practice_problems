import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def get(root, items):
            if root is None:
                items.append("null")
                return

            items.append(str(root.val))

            get(root.left, items)
            get(root.right, items)

        items = []

        get(root, items)

        return ",".join(items)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def get_root(data):

            if not data:
                return

            curr = data.popleft()

            if curr == "null":
                return

            node = TreeNode(curr)

            node.left = get_root(data)

            node.right = get_root(data)

            return node

        items = data.split(",")

        queue = collections.deque()

        for item in items:
            queue.append(item)

        root = get_root(queue)

        return root

root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(5)

c = Codec()
b=c.serialize(root)
d = c.deserialize(b)