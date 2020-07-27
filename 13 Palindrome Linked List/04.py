### Decide whether given linked list is palindrome or not using runner.
###
from datastructure import *
import collections

def is_palindrome(head):

    return True


input_1 = ListNode(1)
input_1.next = ListNode(2)

input_2 = ListNode(1)
input_2.next = ListNode(2)
input_2.next.next = ListNode(2)
input_2.next.next.next = ListNode(1)

print(is_palindrome(input_1))
print(is_palindrome(input_2))