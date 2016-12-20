class Empty:
    def __init__(self):
        return

    def map(self, f):
        return self

    def filter(self, f):
        return self

class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

    def map(self, f):
        return Node(f(self.value), self.tail.map(f))

    def filter(self, f):
        xs = self.tail.filter(f)
        if f(self.value):
            Node(self.value, xs)
        else:
            return xs

l = Node(5, Node(9, Node(-1, Empty())))
l.map(lambda x: x + 2)
l.filter(lambda x: x % 3 == 0)