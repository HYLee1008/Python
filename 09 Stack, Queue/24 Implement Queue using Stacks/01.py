### Implement queue include 4 operations (push, pop, peek, empty) using queue
###
class queue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        return self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


q = queue()

q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())