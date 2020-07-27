### Decide whether given linked list is palindrome or not using list conversion.
###
from datastructure import *

def is_palindrome(head):
    q = []

    if not head:
        return True

    node = head
    # list conversion
    while node is not None:
        q.append(node.val)
        node = node.next

    # determine palindrome
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


input_1 = ListNode(1)
input_1.next = ListNode(2)

input_2 = ListNode(1)
input_2.next = ListNode(2)
input_2.next.next = ListNode(2)
input_2.next.next.next = ListNode(1)

print(is_palindrome(input_1))
print(is_palindrome(input_2))