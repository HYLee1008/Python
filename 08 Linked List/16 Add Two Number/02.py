### Add two reversed number in linked list using full adder
### It's okay but messy.
from datastructure import *

# reverse linked list
def add_two_numbers(l1, l2):
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = add_two_numbers(l1, l2)
while result:
    print(result.val)
    result = result.next