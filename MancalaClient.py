from Human import Human
from Gameboard import Gameboard

p1 = Human("Alden", 1)
p2 = Human("Caroline", 2)

g1 = Gameboard()
print(g1.displayBoard())

while not g1.determineWin(): # calls play methods for player 1 and player 2 while there is no winner
    g1.onePlay(p1, 1)
    print(g1.displayBoard())
    g1.onePlay(p2, 2)
    print(g1.displayBoard())
    g1.determineWin()

if g1.board[0] > g1.board[13]: # if player 1 has the most seeds in their mancala they win
    print("Player 1 wins!")
else: # if player 2 has the most seeds in their mancala they win
    print("Player 2 wins!")


