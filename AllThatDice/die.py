#
# File: die.py
# Description: Game file for die.
# Author: Liam Henke
# Student ID: 110377752
# Email ID: henld003
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

import random

class Die:
    DICE_SYMBOLS = {
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
    }

    def __init__(self):
        self.face_value = 1

    def roll(self, strength=0):
        self.face_value = (random.randint(1, 6) + strength - 1) % 6 + 1
        return self.face_value

    def get_symbol(self):
        return self.DICE_SYMBOLS[self.face_value]
