class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Not Pythonic
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Pythonic
def reverse_linked_list_pythonic(head):
    prev, current = None, head
    while current:
        current.next, prev, current = prev, current, current.next
    return prev