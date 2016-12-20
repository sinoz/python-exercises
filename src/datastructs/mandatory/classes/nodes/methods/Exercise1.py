class Player:
    def __init__(self):
        self.lifepoints = 100

    def Heal(self):
        self.lifepoints += 1

    def Damage(self):
        self.lifepoints -= 1

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def Cheat(self):
        self.player1.Heal()
        self.player2.Damage()

player1 = Player()
player2 = Player()

game = Game(player1, player2)