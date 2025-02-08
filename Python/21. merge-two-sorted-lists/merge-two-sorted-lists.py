# Definition for a singly linked list node 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoListsRecursive(list1, list2):
    if not list1:
        return list2  # If list1 is empty, return list2
    if not list2:
        return list1  # If list2 is empty, return list1

    if list1.val < list2.val:
        list1.next = mergeTwoListsRecursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRecursive(list1, list2.next)
        return list2


# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None  # Return None if the array is empty
    head = ListNode(arr[0])  # Create the head node
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # End of the list

# Example 1: list1 = [1, 2, 4], list2 = [1, 3, 4]
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

print("List 1:")
print_linked_list(list1)
print("List 2:")
print_linked_list(list2)

# Merge the two lists
merged_list = mergeTwoListsRecursive(list1, list2)

print("\nMerged List:")
print_linked_list(merged_list)