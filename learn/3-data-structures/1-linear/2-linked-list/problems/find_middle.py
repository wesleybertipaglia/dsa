class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Not Pythonic
def find_middle(head):
    if not head:
        return None
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    mid = count // 2
    current = head
    for _ in range(mid):
        current = current.next
    return current

# Pythonic
def find_middle_pythonic(head):
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow