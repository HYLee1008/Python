### Swap linked list with pair by value exchange.
### Not a practical method
from datastructure import *

def swap_pairs(head):
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)

result = swap_pairs(input)
while result:
    print(result.val)
    result = result.next