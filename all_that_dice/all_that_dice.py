# all_that_dice.py
#
# File: all_that_dice.py
# Description: Implements the AllThatDice game class.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#


class AllThatDice:
    def __init__(self):
        self.players = []

    def run(self):
        print("Welcome to All-That-Dice!")
        # Main game loop and logic here
        # Example: adding a player
        name = input("Enter player name: ")
        player = Player(name)
        self.players.append(player)
        print(f"Player {name} has been added.")