class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail

def reverse(node):
    last = node
    reversed = None
    while not last is None:
        reversed = Node(last.value, reversed)
        last = last.tail
    return reversed

chain = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
reversedChain = reverse(chain)

def printChain(node):
    n = node
    while not n is None:
        print(n.value)
        n = n.tail

printChain(reversedChain)