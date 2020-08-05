### Make linked list reverse from index m to n by iterative
###
from datastructure import *

def reverse_between(head, m, n):
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    for _ in range(m - 1):
        start = start.next
    end = start.next

    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next


head = ListNode(1)
input = head
for i in [2, 3, 4, 5]:
    head.next = ListNode(i)
    head = head.next

result = reverse_between(input, 2, 4)
while result:
    print(result.val)
    result = result.next