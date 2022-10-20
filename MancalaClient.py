from Human import Human
from Gameboard import Gameboard

p1 = Human("Alden", 1)
p2 = Human("Caroline", 2)

g1 = Gameboard()
print(g1.displayBoard())

while g1.determineWin() != True:
    g1.onePlay(p1, 1)
    print(g1.displayBoard())
    g1.onePlay(p2, 2)
    print(g1.displayBoard())
    g1.determineWin()

if g1.board[0] > g1.board[13]:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")


