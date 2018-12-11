from Cards import *
from random import Random
from random import Random
from datetime import datetime
import time

class Game:
    deck = Deck()
    game = []
    mRandom = Random(datetime.now())

    def __init__(self):
        for suit,rank in self.mRandom.sample(list(self.deck),52):
             self.game.append((suit,rank))

    def __len__(self):
        return len(self.game)

    def __getitem__(self,position):
        return self.game[position]

