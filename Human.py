from Player import Player


class Human(Player):

    def __init__(self, name, num):
        super().__init__(name)
        self.playerNumber = num

    def pickPocket(self):
        print("Player:", self.getName())
        pocket = int(input("Enter the pocket you want to play: "))
        if (self.playerNumber == 1 and pocket < 7) or (self.playerNumber == 2 and pocket > 7):
            # if the player picks from the wrong side of the board it returns an error and asks them to pick again
            print("error, pick from your side of the board (player 1 = pockets 8 - 13, player 2 - pockets 1 - 6)")
            pocket = int(input("Enter the pocket you want to play: "))
        if pocket == 0 or pocket == 7:
            # if the player picks a mancala, it returns an error and asks them to pick again
            print("error, you picked a mancala instead of a pocket, do not enter 0 or 7")
            pocket = int(input("Enter the pocket you want to play: "))
        return pocket

