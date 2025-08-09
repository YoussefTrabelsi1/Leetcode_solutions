class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers_bruteforce(l1, l2):
    def list_to_num(node):
        num, place = 0, 1
        while node:
            num += node.val * place
            place *= 10
            node = node.next
        return num
    
    def num_to_list(num):
        dummy = ListNode()
        curr = dummy
        if num == 0:
            return ListNode(0)
        while num > 0:
            curr.next = ListNode(num % 10)
            curr = curr.next
            num //= 10
        return dummy.next
    
    return num_to_list(list_to_num(l1) + list_to_num(l2))
