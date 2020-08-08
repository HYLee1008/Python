### Merge k sorted lists to single list using priority queue
###
from datastructure import *
import heapq

def merge_k_lists(lists):
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


List_1 = ListNode(1)
List_1.next = ListNode(4)
List_1.next.next = ListNode(5)

List_2 = ListNode(1)
List_2.next = ListNode(3)
List_2.next.next = ListNode(4)

List_3 = ListNode(2)
List_3.next = ListNode(6)

input = [List_1, List_2, List_3]
result = merge_k_lists(input)
while result:
    print(result.val)
    result = result.next