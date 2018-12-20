#https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Note : if there is no intersection both pointers point to None, else they
# point to the intersection
# we can use another list to store all objects but it will cost O(n) space.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        p1, p2 = headA, headB

        while p1 is not p2:
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB

            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA
        return p1