from Player import Player


# noinspection PyPep8Naming
class Gameboard:

    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

    def onePlay(self, p1, oneOrTwo):
        ot = oneOrTwo
        pockStart = p1.pickPocket()
        seeds = self.board[pockStart]
        self.board[pockStart] = 0
        currentPock = pockStart+1
        print("seeds=",seeds)
        for x in range(seeds):
            if (currentPock == 0 and ot == 1) or (currentPock == 7 and ot == 2):
                self.board[currentPock] = self.board[currentPock] + 1
                currentPock = currentPock + 1
            elif (currentPock == 0 and ot == 2) or (currentPock == 7 and ot == 1):
                currentPock = currentPock + 1
                x = x-1
            elif currentPock == 13:
                self.board[currentPock] = self.board[currentPock] + 1
                currentPock = 0
            else:
                self.board[currentPock] = self.board[currentPock] + 1
                currentPock = currentPock + 1

            # also need a variable for the last pocket added 

    def displayBoard(self):
        print(self.board)









