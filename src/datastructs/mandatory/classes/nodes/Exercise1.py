class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

def print(node):
    n = node
    while not n is None:
        print(n.value)
        n = n.tail

print(Node(1, Node(2, Node(3, Node(4, None)))))