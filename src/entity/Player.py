#player.py

from Entity import *

class Player(Entity):
    def __init__(self,name,moveRange,*args,**kwargs):
        #PRECONDITION: all *args MUST be dictionaries (used for subclasses)
        for i in args:
            kwargs.update(i)
        Entity.__init__(self,kwargs)
        
        self.getData()["name"] = name
        self.getData()["moveRange"] = moveRange
        
    #gets the name of the player
    def getName(self):
        return self.getKey("name")
    
    #gets the total steps able to move in one turn
    def getMoveRange(self):
        return self.getKey("moveRange")
