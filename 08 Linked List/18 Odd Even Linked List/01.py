### Make linked list odd number first, even number last by iterative
### O(n)
from datastructure import *

def odd_even_list(head):
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


head = ListNode(1)
input = head
for i in [2, 3, 4, 5]:
    head.next = ListNode(i)
    head = head.next

result = odd_even_list(input)
while result:
    print(result.val)
    result = result.next

