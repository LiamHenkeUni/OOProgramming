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

from player import Player
from game import OddOrEven, Maxi

class AllThatDice:
    def __init__(self):
        self.players = []
        self.total_games_played = 0

    def run(self):
        print("Welcome to All-That-Dice!")
        self.add_player()
        self.main_menu()

    def add_player(self):
        name = input("Enter player name: ")
        player = Player(name)
        self.players.append(player)
        print(f"Player {name} has been added.")

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Play OddOrEven")
            print("2. Play Maxi")
            print("3. Show Player Info")
            print("4. Show Total Games Played")
            print("5. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.play_game(OddOrEven())
            elif choice == '2':
                self.play_game(Maxi())
            elif choice == '3':
                self.show_player_info()
            elif choice == '4':
                self.show_total_games_played()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def show_player_info(self):
        for player in self.players:
            print(f"Player: {player.name}, Chips: {player.chips}, Games Played: {player.games_played}, Games Won: {player.games_won}")

    def increase_total_games_played(self):
        self.total_games_played += 1
        for player in self.players:
            player.increase_games_played()

    def show_total_games_played(self):
        print(f"Total games played: {self.total_games_played}")

    def play_game(self, game):
        print("\nChoose a player for the game:")
        for i, player in enumerate(self.players):
            print(f"{i+1}. {player.name}")
        choice = int(input("Enter the number of the player: ")) - 1
        if 0 <= choice < len(self.players):
            player = self.players[choice]
            winner = game.play(player)
            self.increase_total_games_played()
            if winner == player.name:
                player.increase_games_won()
                print(f"{player.name} has won the game!")
            else:
                print(f"{player.name} has lost the game!")
        else:
            print("Invalid choice.")