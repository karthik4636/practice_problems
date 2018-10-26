#uses no extra space
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
        pass
    




a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
a.next = b
b.next = c