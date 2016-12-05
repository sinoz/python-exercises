class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Player("Henk", Position(0, 2))
p2 = Player("Peter", Position(7, 2))
p3 = Player("Johan", Position(3, 4))