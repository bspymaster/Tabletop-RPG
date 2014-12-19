#player.py

from Entity import *

class Player(Entity):
    """
    Creates a new instance of a player
    @param string a unique name for the player (used when saving)
    @param integer a number greater than or equal to 0 that defines what the distance the player can move is
    @param boolean whether or not, when creating the new object, to create a new set of data from the provided parameters or to load an existing dictionary of information from a file using the name param as a reference
    @param *args a variable amount of dictionaries to append to the data file (not required, MUST be dictionaries)
    @param **kwargs a variable amount of new arguments in the format `keyword = arg` to add to the data dictionary. in this example,`keyword` must be a string, and `arg` can be any type of object. (not required)
    """
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
    
    """
    gets the total steps able to move in one turn
    @return integer the distance the player can move in one turn
    """
    def getMoveRange(self):
        return self.getKey("moveRange")
