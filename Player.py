#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : -

from Cards import *
from Game import *
from itertools import product,permutations
from prettytable import PrettyTable
import numpy as np
import sys
import time

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[97m'  # white


class Player:

    one = []
    two = []
    three = []
    four = []

    one_credit = 100
    two_credit = 100
    three_credit = 100
    four_credit = 100

    one_score = 0
    two_score = 0
    three_score = 0
    four_score = 0

    one_bet = 0
    two_bet = 0
    three_bet = 0
    four_bet = 0

    round_score = 0

    tb = PrettyTable()
    tb.field_names = [G+"Players","Round","Betting","Score","Credits"+W]

    def __init__(self):
        self.tb.field_names = [G+"Players","Round","Betting","Score","Credits"+W]
        self.tb.add_row(["Player One",0,0,0,100])
        self.tb.add_row(["Player Two",0,0,0,100])
        self.tb.add_row(["Player One",0,0,0,100])
        self.tb.add_row(["Player One",0,0,0,100])
        self.welcome()
        print(G+"[*]"+W+" Starting the Game ...\n")
        print(self.tb)


    def start_game(self,r):
        self.new_game = Game()
        self.tb.clear_rows()
        self.clear_all()

        if self.one_credit > 0:
            self.one = self.new_game[0:12]
            print(G+"\n[*]"+W+" Initializing Player "+Y+"One"+W+" ...")
            self.one_score = self.check_score(self.one_score,self.one,"One")
            self.one_bet = self.Set_Score(self.one_bet,self.one,"One",self.one_credit)
            self.one_credit -= self.one_bet
            self.round_score += self.one_bet

        if self.two_credit > 0:
            self.two = self.new_game[13:27]
            print(G+"\n[*]"+W+" Initializing Player "+Y+"Two"+W+" ...")
            self.two_score = self.check_score(self.two_score,self.two,"Two")
            self.two_bet = self.Set_Score(self.two_bet,self.two,"Two",self.two_credit)
            self.two_credit -= self.two_bet
            self.round_score += self.two_bet

        if self.three_credit > 0:
            self.three = self.new_game[27:39]
            print(G+"\n[*]"+W+" Initializing Player "+Y+"Three"+W+" ...")
            self.three_score = self.check_score(self.three_score,self.three,"Three")
            self.three_bet = self.Set_Score(self.three_bet,self.three,"Three",self.three_credit)
            self.three_credit -= self.three_bet
            self.round_score += self.three_bet

        if self.four_credit > 0:
            self.four = self.new_game[30:52]
            print(G+"\n[*]"+W+" Initializing Player "+Y+"Four"+W+" ...")
            self.four_score = self.check_score(self.four_score,self.four,"Four")
            self.four_bet = self.Set_Score(self.four_bet,self.four,"Four",self.four_credit)
            self.four_credit -= self.four_bet
            self.round_score += self.four_bet
        print("\n")
        self.check_win()
        del self.one[0:13]
        self.tb.add_row(["Player One",r,self.one_bet,self.one_score,self.one_credit])
        self.tb.add_row(["Player Two",r,self.two_bet,self.two_score,self.two_credit])
        self.tb.add_row(["Player Three",r,self.three_bet,self.three_score,self.three_credit])
        self.tb.add_row(["Player Four",r,self.four_bet,self.four_score,self.four_credit])

        print(self.tb)

    def clear_all(self):
        self.one_bet = 0
        self.two_bet = 0
        self.three_bet = 0
        self.four_bet = 0

        self.one_score = 0
        self.two_score = 0
        self.three_score = 0
        self.four_score = 0

        self.round_score = 0

    def check_win(self):
        score_list = [int(self.one_score),int(self.two_score),int(self.three_score),int(self.four_score)]
        winner = (list(map(lambda x:21-x,score_list)))
        winner = np.argmin(winner)
        d = False

        if 21 in score_list:
            d = True
            winner = score_list.index(21)


        if winner == 0:
            print(R+"[+] Round Winner : Player One"+W)
            self.one_credit += self.round_score
            if d:
                sys.exit(0)

        elif winner == 1:
            print(R+"[+] Round Winner : Player Two"+W)
            self.two_credit += self.round_score
            if d:
                sys.exit(0)

        elif winner == 2 :
            print(R+"[+] Round Winner : Player Three"+W)
            self.three_credit += self.round_score
            if d:
                sys.exit(0)

        elif winner == 3:
            print(R+"[+] Round Winner : Player Four"+W)
            self.four_credit += self.round_score
            if d:
                sys.exit(0)

    def check_score(self,pl,cr,st):
        for x in cr[:2]:
            if x[0] != "J" and  x[0] != "Q" and x[0] != "K" and x[0] != "A":
                pl += int(x[0])
            if x[0] == "J" or x[0] == "Q" or x[0] == "K":
                pl += 10
            if x[0] == "A":
                _a = int(input(R+"[+]{c} Choose 11 or 1 for {x} : ".format(c =W,x=x)))
                while(_a != 11 and  _a != 1):
                    _a = int(input(R+"[+]{c} Choose 11 or 1 for {x} : ".format(c=W,x=x)))
                pl += _a
        print(G+"[+]{c} Player {st} Score = {cc}{s}{c}".format(cc=B,c=W,s = str(pl),st=st))
        return pl


    def Set_Score(self,pl,cr,st,limit):
        print(G+"[+]{c} 1st Card for Player {st} = {cc}{c}".format(c=W,cc=cr[0],st=st))
        print(G+"[+]{c} 2nd Card for Player {st} = {cc}{c}".format(c=W,cc=cr[1],st=st))
        _b = int(input(B+"[+]{c} Betting Score for Player {st}: ".format(c =W,st=st)))
        while(_b > int(limit) or _b < 0):
            _b = int(input(B+"[+]{c} Betting Score for Player {st}: ".format(c =W,st=st)))
        return _b


    def welcome(self):
            print("""%s


                ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
                ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
                ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝
                ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗
                ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
                ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

                                                                         %s%s
                        # Developpée par Samar Hajj Hassan
                              # Jeu de BlackJack



    """ % (Y, W, G))

if __name__ == "__main__":
    pl = Player()
    pl.start_game(1)
    pl.start_game(2)
    pl.start_game(3)
    pl.start_game(4)
