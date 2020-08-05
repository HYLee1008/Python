### Reverse linked list by recursive
###
from datastructure import *

def reverse_list(head):
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)

reverse = reverse_list(input)
while reverse:
    print(reverse.val)
    reverse = reverse.next