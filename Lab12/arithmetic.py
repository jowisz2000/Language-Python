
class iterator1:

    def __init__(self, first, diff, mx):
        self.first = first
        self.diff = diff
        self.max = mx

    def __iter__(self):
        return self

    def __next__(self):
        self.first += self.diff

        if self.first > self.max:
            raise StopIteration

        return self.first

class iterator2:

    def __init__(self, first, diff, mx):
        self.first = first
        self.diff = diff
        self.max = mx

    def __iter__(self):
        return iterator2(self.first + self.diff, self.diff, self.max)

    def __next__(self):
        self.first += self.diff

        if self.first > self.max:
            raise StopIteration

        return self.first
