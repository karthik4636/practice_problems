
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for i in arr[1:]:
        current.next = ListNode(i)
        current = current.next
    return head
