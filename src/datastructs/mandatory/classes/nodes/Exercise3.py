class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

def sum(node):
    n = node
    sum = 0
    while not n is None:
        sum += n.value
        n = n.tail
    return sum

chain = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
chainSum = sum(chain)

print(chainSum)