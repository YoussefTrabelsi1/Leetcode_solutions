class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    visited = []  # brute force: keep track of visited nodes
    current = head
    while current:
        if current in visited:  # cycle detected
            return True
        visited.append(current)  # mark as visited
        current = current.next
    return False
