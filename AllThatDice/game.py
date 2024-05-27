#
# File: game.py
# Description: Game file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

import random

class Game:
    def play(self, player):
        pass

class OddOrEven(Game):
    def play(self, player):
        print(f"{player.name} is playing OddOrEven game...")
        dice_roll = random.randint(1, 6)
        print(f"Dice rolled: {dice_roll}")
        if dice_roll % 2 == 0:
            print("Even wins!")
            return player.name
        else:
            print("Odd wins!")
            return None

class Maxi(Game):
    def play(self, player):
        print(f"{player.name} is playing Maxi game...")
        dice_rolls = [random.randint(1, 6) for _ in range(3)]
        print(f"Dice rolled: {dice_rolls}")
        if sum(dice_rolls) > 10:
            print(f"{player.name} wins!")
            return player.name
        else:
            print(f"{player.name} loses!")
            return None