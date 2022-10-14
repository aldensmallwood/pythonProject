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
            if (self.board[currentPock] == 0 and oneOrTwo == 1) or (self.board[currentPock] == 7 and oneOrTwo == 2):
                self.board[currentPock] = self.board[currentPock] + 1
            elif (self.board[currentPock] == 0 and oneOrtwo == 2) or (self.board[currentPock] == 7 and oneOrtwo == 1):
                currentPock = currentPock + 1
            elif (self.board[currentPock] == 13):
                self.board[currentPock] = self.board[currentPock] + 1
                currentPock = 0
            else:
                self.board[currentPock] = self.board[currentPock] + 1
                currentPock = currentPock + 1

            # also need a variable for the last pocket added 











