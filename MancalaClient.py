from Human import Human
from Gameboard import Gameboard

p1 = Human("Alden", 1)
g1 = Gameboard()
pock = p1.pickPocket()
print(g1.displayBoard())
g1.onePlay(p1, 1)
print(g1.displayBoard())

