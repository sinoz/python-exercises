class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

def count(node):
    n = node
    count = 0
    while not n is None:
        count += 1
        n = n.tail
    return count

chain = Node(1, Node(2, Node(3, Node(4, None))))
chainLength = count(chain)

print(chainLength)