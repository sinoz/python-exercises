class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

def transform(node, multiplier):
    n = node
    sum = 0
    while not n is None:
        sum += n.value * multiplier
        n = n.tail
    return sum

multiplier = int(input("Insert multiplier"))
chain = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))

chainTransformation = transform(chain, multiplier)

print(chainTransformation)