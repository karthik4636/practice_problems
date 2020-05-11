#https://leetcode.com/problems/find-leaves-of-binary-tree

from collections import defaultdict
class Solution:
    def findLeaves(self, root):
        res = []

        d = defaultdict(list)
        def dfs(node):
            if node == None:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            currHeight = max(leftHeight,rightHeight)+1
            d[currHeight].append(node.val)
            return currHeight
        dfs(root)
        for v in d.values():
            res.append(v)
        return res