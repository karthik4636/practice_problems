# Definition for singly-linked list.
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            current = current.next

        return head



a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
a.next = b
s = Solution()
s.deleteDuplicates(a)
