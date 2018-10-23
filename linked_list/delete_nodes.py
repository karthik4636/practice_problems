# https://leetcode.com/problems/delete-node-in-a-linked-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next






a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
#b.next = c
s = Solution()
s.deleteNode(a)