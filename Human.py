from Player import Player


class Human(Player):

    def __init__(self, name, num):
        super().__init__(name)
        self.playerNumber = num

    def pickPocket(self):
        pocket = int(input("Enter the pocket you want to play: "))
        return pocket

