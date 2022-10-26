

# noinspection PyPep8Naming
class Gameboard:

    def __init__(self):
        self.board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self.currentPock = 0

    def getBoard(self):
        return self.board

    def onePlay(self, p1, oneOrTwo):
        ot = oneOrTwo
        if self.currentPock == 0 or self.currentPock == 7:
            # if the player lands in the mancala pit, they pick a pocket again
            pockStart = p1.pickPocket()
        else: # otherwise it sets the starting pocket to where the player landed
            pockStart = self.currentPock
        seeds = self.board[pockStart]
        self.board[pockStart] = 0
        self.currentPock = pockStart + 1
        print("seeds=", seeds)
        self.displayBoard()

        for x in range(seeds):
            #iterates through the gameboard and places the seeds in pockets
            if self.currentPock == 14: # if the pocket is out of bounds the pocket is set to 0
                self.currentPock = 0
            if self.currentPock == 13: # increment the seeds in pocket 13
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                if x != seeds - 1: # if it is the last seed set pock to zero so it doesn't go out of bounds
                    self.currentPock = 0
            elif (self.currentPock == 0 and ot == 1) or (self.currentPock == 7 and ot == 2):
                # if the player lands in their own mancala increment the mancala seeds
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                if x != seeds - 1:
                    #if it is at the last seed increment the pocket
                    self.currentPock = self.currentPock + 1

            elif (self.currentPock == 0 and ot == 2) or (self.currentPock == 7 and ot == 1):
                # if they land in the other person's pocket, skip it, and add a seed to the next pocket
                self. currentPock = self.currentPock + 1
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                self.currentPock = self.currentPock + 1
                if x == seeds - 1: # if it is at the last seed decrement the current pocket
                    self.currentPock = self.currentPock - 1
            else:
                self.board[self.currentPock] = self.board[self.currentPock] + 1
                # otherwise add a seed to the current pocket and increment current pock
                self.currentPock = self.currentPock + 1
                if x == seeds - 1: # if it is at the last seed decrement current pock
                    self.currentPock = self.currentPock - 1
        self.displayBoard()
        if self.board[self.currentPock] > 1 or self.currentPock == 0 or self.currentPock == 7:
            # if current pocket is zero, seven, or the last pocket has seeds in it call method onePlay again
            self.onePlay(p1, oneOrTwo)

    def displayBoard(self):
        print(" ", self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6])
        print(self.board[0], "           ", self.board[7])
        print(" ", self.board[13], self.board[12], self.board[11], self.board[10], self.board[9], self.board[8])

    def determineWin(self):
        if self.board[1] == 0 and self.board[2] == 0 and self.board[3] == 0 and self.board[4] == 0 and self.board[5] == 0 and self.board[6] == 0:
            # if all the pockets on one side are empty return true
            return True
        elif self.board[8] == 0 and self.board[9] == 0 and self.board[10] == 0 and self.board[11] == 0 and self.board[12] == 0 and self.board[13] == 0:
            # if all the pockets on the other side are empty return true
            return True
        else: # if they aren't empty return false and the code continues
            return False





















