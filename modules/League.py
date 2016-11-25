import Player

class League():
    """Object to represent a league."""
    def __init__(self, players):
        self.players = players

    def addPlayer(name):
        player = Player.Player(name)
        self.players.append(player)

    def printPlayers(self):
        for p in self.players:
            print p.name
