### Swap linked list with pair by recursive.
###
from datastructure import *

def swap_pairs(head):
    if head and head.next:
        p = head.next
        head.next = swap_pairs(p.next)
        p.next = head
        return p
    return head


input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)

result = swap_pairs(input)
while result:
    print(result.val)
    result = result.next