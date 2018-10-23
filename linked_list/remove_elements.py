#https://leetcode.com/problems/remove-linked-list-elements/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        while head.val==val:
            head = head.next
            if head is None:
                return None

        current = head

        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                continue
            current = current.next
        return head




a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
# a.next = b
# b.next = c
s = Solution(
)
s.removeElements(a,1)
