### Merge two sorted list using recur
###
from datastructure import *

def merge_two_lists(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_lists(l1.next, l2)
    return l1


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

merged = merge_two_lists(l1, l2)
while merged:
    print(merged.val)
    merged = merged.next