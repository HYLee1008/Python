### Design circular queue using array
###
class circularqueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    # enQueue(): Move rear point
    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): Move front point
    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


c = circularqueue(5)

print(c.enQueue(10))
print(c.enQueue(20))
print(c.enQueue(30))
print(c.enQueue(40))
print(c.Rear())
print(c.isFull())
print(c.deQueue())
print(c.deQueue())
print(c.enQueue(50))
print(c.enQueue(60))
print(c.Rear())
print(c.Front())
