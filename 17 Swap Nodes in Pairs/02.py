### Swap linked list with pair by iterative.
###
from datastructure import *

def swap_pairs(head):
    root = prev = ListNode(None)
    prev.next = head
    print(id(root), id(prev))
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    return root.next


input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)

result = swap_pairs(input)
while result:
    print(result.val)
    result = result.next