### Sort linked list using built-in function.
###
from datastructure import ListNode


def sort_list(head):
    # liked list to python list
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next

    # sort
    lst.sort()

    # python list to linked list
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    return head