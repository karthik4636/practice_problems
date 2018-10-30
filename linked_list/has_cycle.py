#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = a
s = Solution()
s.hasCycle(a)
