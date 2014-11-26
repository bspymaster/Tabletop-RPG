#player.py

from Entity import *

class Player(Entity):
    def __init__(self,name,moveRange,load,*args,**kwargs):
        #PRECONDITION: load must be True or False
        if not load:
            #PRECONDITION: all *args MUST be dictionaries (used for subclasses)
            for i in args:
                kwargs.update(i)
            Entity.__init__(self,name,load,kwargs)
            
            self.setKey("moveRange",moveRange)
        else:
            Entity.__init__(self,name,load)
    
    #gets the total steps able to move in one turn
    def getMoveRange(self):
        return self.getKey("moveRange")
