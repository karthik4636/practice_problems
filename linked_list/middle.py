#https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        first = head
        second = head
        while True:
            for i in range(2):
                tmp = second.next
                if tmp is None:
                    if i == 0:
                        return first
                    else:
                        return first.next
                else:
                    second = tmp
            first = first.next









a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
#b.next = c
s = Solution()
s.middleNode(a)

