### Add two reversed number in linked list using datatype conversion
### It's okay but messy.
from datastructure import *

# reverse linked list
def reverse_list(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# linked list to python list
def to_list(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list

# python list to linked list
def to_reversed_linkedlist(result):
    prev = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node

# summation of two linked list
def add_two_numbers(l1, l2):
    a = to_list(reverse_list(l1))
    b = to_list(reverse_list(l2))

    result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

    # convert to linked list
    return to_reversed_linkedlist(str(result_str))


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = add_two_numbers(l1, l2)
while result:
    print(result.val)
    result = result.next