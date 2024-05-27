#
# File: main.py
# Description: Main file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

from player import Player
from all_that_dice import OddOrEvenGame, MaxiGame, BuncoGame
from AllThatDice.leaderboard import Leaderboard

class AllThatDice:
    def __init__(self):
        self.players = {}

    def register_player(self):
        name = input("What is the name of the new player? ")
        if name in self.players:
            print("Sorry, the name is already taken.")
        else:
            player = Player(name)
            self.players[name] = player
            print(f"Welcome, {name}!")

    def show_leader_board(self):
        Leaderboard.show(self.players)

    def play_game(self):
        game_choice = input("Which game would you like to play? (o) Odd-or-Even, (m) Maxi, (b) Bunco: ")
        if game_choice == 'o':
            game = OddOrEvenGame()
            if len(self.players) < 1:
                print("Not enough players to play Odd-or-Even.")
                return
            player_name = input("What is the name of the player? ")
            if player_name not in self.players:
                print(f"There is no player named {player_name}.")
                return
            bid = int(input(f"How many chips would you bid {player_name} (1-{self.players[player_name].chips})? "))
            game.add_player(self.players[player_name], bid)
            guess = input(f"Hey {player_name}, Odd (o) or Even (e)? ")
            game.set_guess(self.players[player_name], guess)
            game.start_game()
            game.determine_winner()
        elif game_choice == 'm':
            game = MaxiGame()
            num_players = int(input("How many players (3-5)? "))
            if len(self.players) < num_players:
                print("Not enough players to play Maxi.")
                return
            for i in range(num_players):
                player_name = input(f"What is the name of player #{i + 1}? ")
                if player_name not in self.players:
                    print(f"There is no player named {player_name}.")
                    return
                bid = int(input(f"How many chips would you bid {player_name} (1-{self.players[player_name].chips})? "))
                game.add_player(self.players[player_name], bid)
            game.start_game()
            game.determine_winner()
        elif game_choice == 'b':
            game = BuncoGame()
            num_players = int(input("How many players (2-4)? "))
            if len(self.players) < num_players:
                print("Not enough players to play Bunco.")
                return
            for i in range(num_players):
                player_name = input(f"What is the name of player #{i + 1}? ")
                if player_name not in self.players:
                    print(f"There is no player named {player_name}.")
                    return
                bid = int(input(f"How many chips would you bid {player_name} (1-{self.players[player_name].chips})? "))
                game.add_player(self.players[player_name], bid)
            game.start_game()
            game.play_round()
            game.determine_winner()

    def quit(self):
        print("Thank you for playing All-That-Dice!")
        exit()

    def main_menu(self):
        while True:
            print("What would you like to do?")
            print("(r) register a new player")
            print("(s) show the leader board")
            print("(p) play a game")
            print("(q) quit")
            choice = input("> ")
            if choice == 'r':
                self.register_player()
            elif choice == 's':
                self.show_leader_board()
            elif choice == 'p':
                self.play_game()
            elif choice == 'q':
                self.quit()

if __name__ == "__main__":
    AllThatDice().main_menu()
