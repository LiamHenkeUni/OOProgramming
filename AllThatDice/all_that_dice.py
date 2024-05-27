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

from game import Game

class OddOrEvenGame(Game):
    def __init__(self):
        super().__init__()
        self.guess = {}

    def set_guess(self, player, guess):
        self.guess[player] = guess

    def determine_winner(self):
        for player in self.players:
            strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
            die_value, symbol = self.throw_die(strength)
            print(f"{player.name} guessed {self.guess[player]}, rolled {symbol} ({die_value})")
            if (die_value % 2 == 0 and self.guess[player] == 'e') or (die_value % 2 != 0 and self.guess[player] == 'o'):
                player.add_chips(sum(self.bids.values()))
                print(f"Congratulations, {player.name}! You win!")
                player.increment_games_won()
            else:
                print(f"Sorry, {player.name}! You lose.")
        self.end_game()

class MaxiGame(Game):
    def determine_winner(self):
        max_sum = 0
        winners = []

        for player in self.players:
            strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
            die1_value, die1_symbol = self.throw_die(strength)
            die2_value, die2_symbol = self.throw_die(strength)
            total = die1_value + die2_value
            print(f"{player.name} rolled {die1_symbol} ({die1_value}) and {die2_symbol} ({die2_value}) for a total of {total}")

            if total > max_sum:
                max_sum = total
                winners = [player]
            elif total == max_sum:
                winners.append(player)

        if len(winners) > 1:
            print("Tie! Rolling again.")
            for player in winners:
                self.players.remove(player)
                self.add_player(player, self.bids[player])
            self.determine_winner()
        else:
            winner = winners[0]
            winner.add_chips(sum(self.bids.values()))
            print(f"Congratulations, {winner.name}! You win!")
            winner.increment_games_won()
        self.end_game()

class BuncoGame(Game):
    def __init__(self):
        super().__init__()
        self.rounds = 6
        self.scores = {}
        self.buncos = {}

    def add_player(self, player, bid):
        super().add_player(player, bid)
        self.scores[player] = [0] * self.rounds
        self.buncos[player] = 0

    def play_round(self):
        for round_num in range(1, self.rounds + 1):
            for player in self.players:
                points = 0
                while True:
                    strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
                    die1_value, die1_symbol = self.throw_die(strength)
                    die2_value, die2_symbol = self.throw_die(strength)
                    die3_value, die3_symbol = self.throw_die(strength)
                    round_points = 0
                    if die1_value == die2_value == die3_value:
                        if die1_value == round_num:
                            round_points = 21
                            self.buncos[player] += 1
                        else:
                            round_points = 5
                    elif die1_value == round_num or die2_value == round_num or die3_value == round_num:
                        round_points = 1

                    points += round_points
                    if round_points == 0:
                        break
                self.scores[player][round_num-1] = points
                print(f"{player.name} rolled {die1_symbol}, {die2_symbol}, {die3_symbol} and scored {points} points in round {round_num}")

    def determine_winner(self):
        max_points = 0
        winner = None
        for player, scores in self.scores.items():
            total_points = sum(scores)
            if total_points > max_points:
                max_points = total_points
                winner = player

        if winner:
            winner.add_chips(sum(self.bids.values()))
            print(f"Congratulations, {winner.name}! You win the Bunco game!")
            winner.increment_games_won()
        self.end_game()
