from random import randrange

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class RockPaperScissors:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.winner = None

p1 = Player("Henk", 0)
p2 = Player("Jan", 0)
game = RockPaperScissors(p1, p2)

Rock = 0
Paper = 1
Scissors = 2

WinStrategies = {
    Rock : Scissors, # Rock wins over Scissors
    Scissors : Paper, # Scissors wins over Paper
    Paper : Rock, # Paper wins over Rock
}

def play():
    p1Choice = randrange(2)
    p2Choice = randrange(2)
    if p2Choice == WinStrategies[p1Choice]:
        p2.score += 1
    elif p1Choice == WinStrategies[p2Choice]:
        p1.score += 1

def declareWinnerIfPresent():
    if p1.score == 3 and p2.score != 3:
        game.winner = p1
    elif p2.score == 3 and p1.score != 3:
        game.winner = p2

    if game.winner is not None:
        print("Winner: " + game.winner.name)

while game.winner is None:
    play()
    declareWinnerIfPresent()