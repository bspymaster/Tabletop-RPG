#player.py

from Entity import *

class Player(Entity):
    def __init__(self,name,range):
        Entity.__init__(self)
        self.name = name
        self.moveRange = range
    
    #gets the name of the player
    def getName(self):
        return self.name
    
    #gets the total steps able to move in one turn
    def getMoveRange(self):
        return self.moveRange
