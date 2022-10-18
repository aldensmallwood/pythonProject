from Human import Human
from Gameboard import Gameboard

p1 = Human("Alden", 1)
g1 = Gameboard()
print(g1.displayBoard())
g1.onePlay(p1, 1)
print(g1.displayBoard())

# we need to make sure that when one play iterates again, they are picking up the same pocket it ended in to play