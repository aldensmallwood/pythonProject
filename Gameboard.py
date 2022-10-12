from Player import Player
class Gameboard:

    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

    def onePlay(self, p1):
        pockStart = p1.pickPocket()
        currentPock = pockStart
        seeds = board[pock]
        for x in seeds:






