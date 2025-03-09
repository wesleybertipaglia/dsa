class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Not Pythonic
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Pythonic
def remove_duplicates_pythonic(head):
    current = head
    while current:
        if current.next and current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head