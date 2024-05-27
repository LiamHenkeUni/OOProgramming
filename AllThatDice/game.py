#
# File: game.py
# Description: Game file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from die import Die

class Game:
    def __init__(self):
        self.players = []
        self.bids = {}

    def add_player(self, player, bid):
        if player.chips >= bid:
            self.players.append(player)
            self.bids[player] = bid
            player.deduct_chips(bid)
        else:
            print(f"{player.name} doesn't have enough chips.")

    def start_game(self):
        for player in self.players:
            player.increment_games_played()

    def end_game(self):
        self.players = []
        self.bids = {}

    def throw_die(self, strength):
        die = Die()
        die_value = die.roll(strength)
        symbol = die.get_symbol()
        return die_value, symbol
