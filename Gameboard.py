from Player import Player


# noinspection PyPep8Naming
class Gameboard:

    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self.currentPock = 0

    def onePlay(self, p1, oneOrTwo):
        ot = oneOrTwo
        pockStart = p1.pickPocket()
        seeds = self.board[pockStart]
        self.board[pockStart] = 0
        self.currentPock = pockStart + 1
        print("seeds=",seeds)
        for x in range(seeds):
            if (self.currentPock == 0 and ot == 1) or (self.currentPock == 7 and ot == 2):
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                self.currentPock = self.currentPock + 1
            elif (self.currentPock == 0 and ot == 2) or (self.currentPock == 7 and ot == 1):
                self. currentPock = self.currentPock + 1
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                self.currentPock = self.currentPock + 1
            elif self.currentPock == 13:
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                self.currentPock = 0
            else:
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                self.currentPock = self.currentPock + 1

            # also need a variable for the last pocket added 

    def displayBoard(self):
        print(" ", self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6])
        print(self.board[0], "           ", self.board[7])
        print(" ", self.board[13], self.board[12], self.board[11], self.board[10], self.board[9], self.board[8])
















