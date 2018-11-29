# Definition for singly-linked list.
#https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val > l2.val:
            l1,l2 = l2,l1

        t1 = l1
        t2 = l2

        while t1 is not None and t1.next is not None and t2 is not None:

            a = t1
            b = t1.next
            while t2 is not None:
                if t2.val >= a.val and t2.val <= b.val:
                   tmp = t2.next
                   a.next = t2
                   t2.next = b
                   t1 = b
                   t2 = tmp
                   a = a.next
                else:
                    t1 = b
                    break
        if t1 and t2 is not None:
            t1.next = t2
        return l1








a = ListNode(-7)
b = ListNode(2)
c = ListNode(4)
# a.next = b
# b.next = c

a1 = ListNode(-10)
b1 = ListNode(-10)
c1 = ListNode(-9)
d1 = ListNode(-4)
e1 = ListNode(1)
f1 = ListNode(6)
g1= ListNode(6)
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
e1.next = f1
f1.next = g1

s = Solution()
s.mergeTwoLists(a, a1)
