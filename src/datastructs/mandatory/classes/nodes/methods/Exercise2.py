class Empty:
    def __init__(self):
        return

    def IsEmpty(self):
        return True

    def Length(self):
        return 0

    def Sum(self):
        return 0

class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

    def IsEmpty(self):
        return False

    def Length(self):
        return 1 + self.tail.Length()

    def Sum(self):
        return self.value + self.tail.Sum()

l = Node(5, Node(9, Node(-1, Empty())))
print(l.IsEmpty())