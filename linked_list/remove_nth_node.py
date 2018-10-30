#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        current = head
        count = 0
        while current is not None:
            current = current.next
            count+=1
        count_to_n = count - n -1
        current = head
        if count_to_n == -1:
            if current.next is not None:
                tmp =current.next
            else:
                return None
            current.next = None
            return tmp
        current = head
        while current is not None and current.next is not None:
            if count_to_n == 0:
                current.next = current.next.next
                break

            current = current.next
            count_to_n -= 1
        return head








a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
#b.next = c



s = Solution()
a=s.removeNthFromEnd(a,2)
b=1