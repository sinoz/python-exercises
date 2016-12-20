class Empty:
    def __init__(self):
        return

    def Length(self):
        return 0

    def Sum(self):
        return 0

    def map(self, f):
        return self

    def fold(self, z, f):
        return 0

    def filter(self, f):
        return self

class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

    def map(self, f):
        return Node(self.fold(self.value, lambda x, y: f(x)), self.tail.map(f))

    def Length(self):
        return self.fold(1, lambda x, y: x + self.tail.Length())

    def Sum(self):
        return self.fold(self.value, lambda x, y: x + self.tail.Sum())

    def filter(self, f):
        xs = self.tail.filter(f)
        if f(self.value):
            return self.fold(self, lambda x, y: Node(self.value, xs))
        else:
            return xs

    def fold(self, z, f):
        return f(z, self.tail.fold(z, f))

l = Node(5, Node(9, Node(-1, Empty())))
print(l.filter(lambda x: x % 3 == 0))
