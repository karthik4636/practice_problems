class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        p1,p2 = head, head

        while p2 is not None and p2.next is not None:
             p1 = p1.next
             p2 = p2.next.next

        mid = p1
        cur =mid
        previous = None
        while cur is not None:
            cur_next_copy = cur.next
            cur.next = previous
            previous, cur = cur, cur_next_copy

        cur = head
        while cur is not None and previous is not None:
            copy_cur_next = cur.next
            previous_next_copy = previous.next
            cur.next = previous
            previous.next = copy_cur_next
            cur, previous = copy_cur_next, previous_next_copy
        if cur is not None:
            cur.next = None


from helpers.create_linked_list import create_linked_list

head = create_linked_list([1,2,3,4,5])
s= Solution()
s.reorderList(head)

