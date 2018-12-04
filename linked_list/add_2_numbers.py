# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while p1 is not None or p2 is not None:
            if p1 is None:
                p1_val = 0
            else:
                p1_val = p1.val
            if p2 is None:
                p2_val = 0
            else:
                p2_val = p2.val

            sum = (carry + p1_val + p2_val)
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next


s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

a1 = ListNode(6)
b1 = ListNode(1)
c1 = ListNode(-9)
d1 = ListNode(-4)
e1 = ListNode(1)
f1 = ListNode(6)
g1 = ListNode(6)
a1.next = b1
# b1.next = c1
# c1.next = d1
# d1.next = e1
# e1.next = f1
# f1.next = g1
s.addTwoNumbers(a, a1)
