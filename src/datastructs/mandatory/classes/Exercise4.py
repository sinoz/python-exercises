class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Game:
    def __init__(self, title, p1, p2):
        self.title = title
        self.p1 = p1
        self.p2 = p2

p1 = Player("Henk", Position(0, 2))
p2 = Player("Peter", Position(7, 2))

game = Game("Ganzenbord", p1, p2)