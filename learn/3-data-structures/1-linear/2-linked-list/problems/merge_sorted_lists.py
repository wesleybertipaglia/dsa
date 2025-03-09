class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Not Pythonic
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

# Pythonic
def merge_sorted_lists_pythonic(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        tail.next, l1, l2 = (l1, l1.next) if l1.val < l2.val else (l2, l2.next)
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next