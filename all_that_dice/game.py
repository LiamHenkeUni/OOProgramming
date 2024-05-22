#
# File: game.py
# Description: Game file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

class Game:
    def play(self):
        pass

class OddOrEven(Game):
    def play(self):
        # Implementation for OddOrEven game
        pass

class Maxi(Game):
    def play(self):
        # Implementation for Maxi game
        pass

class OddOrEven(Game):
    def play(self):
        # Specific implementation for OddOrEven
        pass

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")

class Player:
    """
    Represents a player in the All-That-Dice game.
    
    Attributes:
        name (str): The name of the player.
        chips (int): The number of chips the player has.
        games_played (int): The number of games the player has played.
        games_won (int): The number of games the player has won.
    """
    def __init__(self, name):
        """
        Initializes a new player with the given name.
        
        Args:
            name (str): The name of the player.
        """
        self._name = name
        self._chips = 0
        self._games_played = 0
        self._games_won = 0
        
class AllThatDice:
    def __init__(self):
        self.players = []

    def run(self):
        pass