#
# File: player.py
# Description: Player file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

class Player:
    def __init__(self, name):
        self._name = name
        self._chips = 0
        self._games_played = 0
        self._games_won = 0
        
    @property
    def name(self):
        return self._name
    
    def increase_chips(self, amount):
        self._chips += amount
    
    def decrease_chips(self, amount):
        if self._chips >= amount:
            self._chips -= amount
        
    def increase_games_played(self):
        self._games_played += 1
        
    def increase_games_won(self):
        self._games_won += 1

@property
def chips(self):
    return self._chips