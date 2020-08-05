### Implement stack include 4 operations (push, pop, top, empty) using queue
###
from collections import deque

class stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


s = stack()

s.push(1)
s.push(2)
print(s.top())
print(s.pop())
print(s.empty())