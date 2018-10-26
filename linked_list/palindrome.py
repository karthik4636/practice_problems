# Definition for singly-linked list.
# https://leetcode.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        a = []
        current = head
        while current is not None:
            a.append(current.val)
            current = current.next
        current = head
        while current is not None:
            if current.val != a.pop(-1):
                return False
            current = current.next
        return True



a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
a.next = b
b.next = c

s = Solution()
s.isPalindrome(a)
b=1