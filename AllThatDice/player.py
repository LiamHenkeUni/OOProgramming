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
        self.name = name
        self.chips = 100
        self.games_played = 0
        self.games_won = 0

    def place_bid(self, chips):
        if chips <= self.chips:
            self.chips -= chips
            return chips
        else:
            return 0

    def add_chips(self, amount):
        self.chips += amount

    def deduct_chips(self, amount):
        self.chips -= amount

    def increment_games_played(self):
        self.games_played += 1

    def increment_games_won(self):
        self.games_won += 1

    def __str__(self):
        return f"{self.name} - Chips: {self.chips}, Games Played: {self.games_played}, Games Won: {self.games_won}"
