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
            strength = self.get_throw_strength(player)
            die_value, symbol = self.throw_die(strength)
            print(f"{player.name} guessed {self.guess[player]}, rolled {symbol} ({die_value})")
            if (die_value % 2 == 0 and self.guess[player] == 'e') or (die_value % 2 != 0 and self.guess[player] == 'o'):
                player.add_chips(sum(self.bids.values()))
                print(f"Congratulations, {player.name}! You win!")
                player.increment_games_won()
            else:
                print(f"Sorry, {player.name}! You lose.")
        self.end_game()

    def get_throw_strength(self, player):
        while True:
            try:
                strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
                if 0 <= strength <= 5:
                    return strength
                else:
                    print("Strength must be between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 5.")

class MaxiGame(Game):
    def determine_winner(self):
        max_sum = 0
        winners = []

        for player in self.players:
            strength = self.get_throw_strength(player)
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
            winner.add_chips(self.bids[winner] + sum(bid for player, bid in self.bids.items() if player != winner))
            print(f"Congratulations, {winner.name}! You win!")
            winner.increment_games_won()
        self.end_game()

    def get_throw_strength(self, player):
        while True:
            try:
                strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
                if 0 <= strength <= 5:
                    return strength
                else:
                    print("Strength must be between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 5.")

class BuncoGame(Game):
    def __init__(self):
        super().__init__()
        self.rounds = 6
        self.scores = {}
        self.buncos = {}
        self.bids = {}

    def add_player(self, player, bid):
        super().add_player(player, bid)
        self.scores[player] = [0] * self.rounds
        self.buncos[player] = 0
        self.bids[player] = bid

    def set_bid(self, player, bid):
        self.bids[player] = bid

    def play_round(self):
        for round_num in range(1, self.rounds + 1):
            round_scores = {}  # Dictionary to store scores for each player in this round
            print("=" * 34)
            print(f"Round {round_num}")
            print("=" * 34)
            for player in self.players:
                points = 0
                while True:
                    strength = self.get_throw_strength(player)
                    die1_value, die1_symbol = self.throw_die(strength)
                    die2_value, die2_symbol = self.throw_die(strength)
                    die3_value, die3_symbol = self.throw_die(strength)

                    # Calculate points for this roll
                    round_points = 0
                    if die1_value == die2_value == die3_value == round_num:
                        round_points = 21
                        self.buncos[player] += 1
                    elif die1_value == die2_value == die3_value:
                        round_points = 5
                    elif die1_value == round_num or die2_value == round_num or die3_value == round_num:
                        round_points = 1

                    points += round_points

                    # Print dice values and score for this roll
                    print(f"{player.name} rolled: {die1_symbol}, {die2_symbol}, {die3_symbol} for a score of {round_points}")

                    # Check if player scores points and allow them to roll again
                    if round_points == 0 or round_num == self.rounds:
                        print(f"You earned {round_points}, {points} points in total.")
                        break

                round_scores[player] = points

            # Update scores for this round
            for player, points in round_scores.items():
                self.scores[player][round_num - 1] = points
                

    def determine_winner(self):
        total_scores = {player: sum(scores) for player, scores in self.scores.items()}
        max_score = max(total_scores.values())
        winners = [player for player, score in total_scores.items() if score == max_score]

        print("=" * 34)
        print("Game Summary")
        print("=" * 34)
        for player in self.players:
            print(f"{player.name} total score: {total_scores[player]} with {self.buncos[player]} Buncos")
        print("=" * 34)

        if len(winners) == 1:
            winner = winners[0]
            # Add the winner's bid amount to their total chips
            winner.add_chips(self.bids[winner] + sum(bid for player, bid in self.bids.items() if player != winner))
            print(f"Congratulations, {winner.name}! You win with a total score of {max_score} and {self.buncos[winner]} Buncos!")
            winner.increment_games_won()
        else:
            print("It's a tie!")

    def get_throw_strength(self, player):
        while True:
            try:
                strength = int(input(f"How strong will you throw, {player.name}? (0-5) "))
                if 0 <= strength <= 5:
                    return strength
                else:
                    print("Strength must be between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 5.")