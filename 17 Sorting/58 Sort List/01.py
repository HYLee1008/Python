### Sort linked list using merge sort.
### O(nlogn)
from datastructure import ListNode


def merge_two_lists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_two_lists(l1.next, l2)

    return l1 or l2

def sort_list(head):
    if not (head and head.next):
        return head

    # Use runner method
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None

    l1 = sort_list(head)
    l2 = sort_list(slow)

    return merge_two_lists(l1, l2)