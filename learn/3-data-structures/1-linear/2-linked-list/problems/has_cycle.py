class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Not Pythonic
def has_cycle(head):
    nodes_seen = set()
    current = head
    while current:
        if current in nodes_seen:
            return True
        nodes_seen.add(current)
        current = current.next
    return False

# Pythonic
def has_cycle_pythonic(head):
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False