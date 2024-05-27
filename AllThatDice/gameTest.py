#
# File: gameTest.py
# Description: Main test file for dice game.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

import unittest
from player import Player
from game import Game
from all_that_dice import OddOrEvenGame, MaxiGame, BuncoGame

class TestAllThatDice(unittest.TestCase):
    def test_player_creation(self):
        # Test player creation
        player = Player("TestPlayer")
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player.chips, 100)

    def test_game_creation(self):
        # Test game creation
        game = Game()
        self.assertEqual(game.players, [])
        self.assertEqual(game.bids, {})

    def test_odd_or_even_game(self):
        # Test OddOrEvenGame class
        game = OddOrEvenGame()
        player1 = Player("Player1")
        player2 = Player("Player2")
        game.add_player(player1, 10)
        game.add_player(player2, 20)
        self.assertEqual(len(game.players), 2)
        self.assertEqual(len(game.bids), 2)
        # Add more tests for OddOrEvenGame class

    def test_maxi_game(self):
        # Test MaxiGame class
        game = MaxiGame()
        player1 = Player("Player1")
        player2 = Player("Player2")
        game.add_player(player1, 10)
        game.add_player(player2, 20)
        self.assertEqual(len(game.players), 2)
        self.assertEqual(len(game.bids), 2)
        # Add more tests for MaxiGame class

    def test_bunco_game(self):
        # Test BuncoGame class
        game = BuncoGame()
        player1 = Player("Player1")
        player2 = Player("Player2")
        game.add_player(player1, 10)
        game.add_player(player2, 20)
        self.assertEqual(len(game.players), 2)
        self.assertEqual(len(game.bids), 2)
        # Add more tests for BuncoGame class

if __name__ == '__main__':
    unittest.main()
