# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iterative
        if head is None:
            return None

        current = head
        previous = None

        while current is not None:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        return previous











a = ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next =b
b.next = c

s= Solution()
s.reverseList(a)