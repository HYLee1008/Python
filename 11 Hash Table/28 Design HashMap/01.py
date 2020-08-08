### Design hashmap (put, get, remove) using separate chaining
###
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # insert
    def put(self, key, value):
        index = key % self.size
        # when there is no node in the index
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # when there is node
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # inquire
    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # when node exists
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # delete
    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        # when first node of index
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # delete linked list node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
print(hashMap.remove(2))
print(hashMap.get(2))