from Gameboard import Gameboard
from Player import Player
class Game:
    def __init__(self):
        self.player = Player.getName()
        self.board = Gameboard.getBoard()

    def takeTurn(self, p1):

