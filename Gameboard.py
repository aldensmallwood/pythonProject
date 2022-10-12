from Player import Player


# noinspection PyPep8Naming
class Gameboard:

    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

    def onePlay(self, p1, oneOrTwo):
        pockStart = p1.pickPocket()
        currentPock = pockStart
        seeds = self.board[pockStart]
        for x in seeds:
             #  if we are in one of the mancalas, either add one or skip over it
             #  if we are at the end of the mancala board, go back to 0 if that is their mancala, or one if it is not theirs










