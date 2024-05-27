#
# File: leaderboard.py
# Description: Leaderboard file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

class Leaderboard:
    def show(players):
        sorted_players = sorted(players.values(), key=lambda p: (-p.chips, -(p.games_won / p.games_played if p.games_played > 0 else 0)))
        print("=============================")
        print("Name Played Won Chips")
        print("=============================")
        for player in sorted_players:
            print(f"{player.name} {player.games_played} {player.games_won} {player.chips}")
        print("=============================")