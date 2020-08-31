### Insertion sort
###
from datastructure import ListNode


def insertion_sort_list(head):
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        cur = parent
    return cur.next