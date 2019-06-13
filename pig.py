import random

class PlayGame(All the things):
    # will choose a Player to go first (person or computer)
    # will declare winner when a Player reaches a TotalScore of 100
    pass

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class Player:
    def __init__(self, person, computer):
        self.person = person
        self.computer = computer

class Turn(): <Player, Die roll?, TurnScore?>
    # When either the person or computer(Player) rolls the die(Die roll). 
    # Maybe has a score_keeping method?
    pass

class TurnScore(): <Player, Die>
    # will calculate turn score for each Player(person or computer)
    # will be 0 or a sum of Die roll
    pass

class TotalScore(): <TurnScore, Player>
    # will be the sum of TurnScore for each Player(person or computer)
    pass


# die = Die()
# rolled = die.roll()
# print(rolled)

