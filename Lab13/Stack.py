
class Stack:

    def __init__(self, other=[]):
        self.stack = []
        if other:
            for i in other.stack:
                self.stack.extend(i)

    def push_single(self, other):
        self.stack.append(other)

    def push_multiple(self, other):
        for i in other.stack:
            self.stack.append(i)

    def pop(self):
        del self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


class SortedStack(Stack):

    def push_single(self, other):

        if not self.stack:
            self.stack.append(other)

        if other > self.stack[-1]:
            self.stack.append(other)


