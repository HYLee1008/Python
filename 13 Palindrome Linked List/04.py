### Decide whether given linked list is palindrome or not using runner.
### Fastest method. No data structure conversion.
from datastructure import *
import collections

def is_palindrome(head):
    rev = None
    slow = fast = head
    # Make reverse linked list using runner
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    ### check palindrome
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


input_1 = ListNode(1)
input_1.next = ListNode(2)

input_2 = ListNode(1)
input_2.next = ListNode(2)
input_2.next.next = ListNode(2)
input_2.next.next.next = ListNode(1)

print(is_palindrome(input_1))
print(is_palindrome(input_2))