import random
def dice_roll():
    x = random.randint(1,6)
    y = random.randint(1,6)
    return (f"({x},{y})")
print(dice_roll())














"""
import random
class Dice:
    def roll_dice():
        x = random.randint(1,6)
        y = random.randint(1,6)
        print(f"({x},{y})")

Dice.roll_dice()
from Speed.RollDice import Dice
Dice.roll()
"""
