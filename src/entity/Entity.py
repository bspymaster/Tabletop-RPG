#entity.py

import pickle
"""
Standard class for all entities that go on the grid; able to hold a variable amount of information in a dictionary
"""
class Entity:
    """
    Creates a new instance of an entity
    @param string a unique name for the entity (used when saving)
    @param boolean whether or not, when creating the new object, to create a new set of data from the provided parameters or to load an existing dictionary of information from a file using the name param as a reference
    @param *args a variable amount of dictionaries to append to the data file (not required, MUST be dictionaries)
    @param **kwargs a variable amount of new arguments in the format `keyword = arg` to add to the data dictionary. in this example,`keyword` must be a string, and `arg` can be any type of object. (not required)
    """
    def __init__(self,name,load,*args,**kwargs):
        if not load:
            self.data = kwargs
            self.setKey("name",name)
            #used for subclass data sets
            for i in args:
                self.getData().update(i)
        else:
            self.load(name)
    """
    adds a new key to the data dictionary
    @param string the name of the keyword to add to the dictionary (must not be the same as an existing keyword
    
    """
    def setKey(self,key,value):
        self.getData()[key] = value
        return True
    
    """
    removes the key and value with the given key name
    @param string the specific key and value pair whose key is in getData that will be removed
    @return tuple the (key,value) pair that was removed, otherwise returns None if the key was not found
    """
    def removeKey(self,key):
        if key in self.getData():
            value = self.getKey(key)
            del self.getData()[key]
            return (key,value)
        else:
            return None
    
    """
    Gets the unique name of the entity
    @return string the name of the entity
    """
    def getName(self):
        return self.getKey("name")
    
    """
    gets the dynamic dictionary of data stored for the entity
    @return dictionary the dictionary of information used for the entity
    """
    def getData(self):
        return self.data
        """ use this code for printing the items contained in the data dictionary
        for k,v in self.data.iteritems():
            print "%s = %s" % (k, v)
        """
    
    """
    gets the value at the specific key index
    @param string the unique key in the data dictionary that has the value to be used
    @return object the information stored at the key's location, if the key is not in the data, returns None
    """
    def getKey(self,key):
        if key in self.getData():
            return self.getData()[key]
        else:
            return None
    
    """
    saves current object and all data to *.ent in the saves folder. The `*` is replaced by the unique name that each entity has
    """
    def save(self):
        saveFile = open("saves/%s.ent" % self.getName(),"wb")
        pickle.dump(self.data,saveFile)
        saveFile.close()
    
    """
    loads a premade object with all data
    @param string sets the entity's data to previously saved data from *.ent, replacing `*` with the parameter
    """
    def load(self,name):
        saveFile = open("saves/%s.ent" % name,"rb")
        self.data = pickle.load(saveFile)
        saveFile.close()
