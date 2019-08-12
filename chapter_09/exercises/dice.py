from random import randint


class Dice:
    """A simple model of a Dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(f'Rolling the {self.sides} dice...')
        print(f"The number on the dice is...\n{randint(1,self.sides)}")


dice_10 = Dice(10)
dice_20 = Dice(20)

for _ in range(1, 11):
    dice_10.roll_dice()

for _ in range(1, 11):
    dice_20.roll_dice()
