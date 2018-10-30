#https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        prev = head
        head = head.next
        curr= prev.next
        while prev is not None and curr is not None:
            next = curr.next
            prev.next =curr.next
            curr.next = prev
            if next and next.next:
                prev.next = next.next
            else:
                prev.next = next

            prev = next

            if  prev is None:
                break
            curr = prev.next
        return head











a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b

b.next = c



s = Solution()
a=s.swapPairs(a)
b=1