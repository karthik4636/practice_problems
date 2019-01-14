#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        ans, cur, temp, flag = [], [root], [], 1
        while cur:
            ans.append(list(x.val for x in cur[::flag]))
            for node in cur:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            cur, temp = temp, []
            flag *= -1

        return ans