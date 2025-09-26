class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    visited = set()
    current = head
    while current:
        if current in visited:  # already visited = cycle
            return True
        visited.add(current)  # add to visited set
        current = current.next
    return False
