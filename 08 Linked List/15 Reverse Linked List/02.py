### Reverse linked list by iterative
### Iterative consumes 70% memory of the recursive method. And slightly faster.
from datastructure import *

def reverse_list(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)

reverse = reverse_list(input)
while reverse:
    print(reverse.val)
    reverse = reverse.next