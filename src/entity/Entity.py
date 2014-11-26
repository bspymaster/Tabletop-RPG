#entity.py

import pickle

class Entity:
    def __init__(self,name,load,*args,**kwargs):
        #PRECONDITION: load must be True or False
        if not load:
            self.data = kwargs
            self.setKey("name",name)
            #PRECONDITION: all *args MUST be dictionaries (used for subclasses)
            for i in args:
                self.getData().update(i)
        else:
            self.load(name)
    
    #adds a new key to the data dictionary
    def setKey(self,key,value):
        self.getData()[key] = value
        return True
    
    #removes the key with the target index and returns the key,value pair as a tuple
    def removeKey(self,key):
        value = self.getKey(key)
        del self.getData()[key]
        return (key,value)
    
    #gets the name of the entity
    def getName(self):
        return self.getKey("name")
    
    #gets the dynamic dictionary of data stored for the object
    def getData(self):
        return self.data
        """ use this code for printing the items contained in the data dictionary
        for k,v in self.data.iteritems():
            print "%s = %s" % (k, v)
        """
    
    #gets the value at the specific key index
    def getKey(self,key):
        return self.getData()[key]
    
    #saves current object and all stats
    def save(self):
        saveFile = open("saves/%s.ent" % self.getName(),"wb")
        pickle.dump(self.data,saveFile)
        saveFile.close()
    
    #loads a premade object with all stats
    def load(self,name):
        saveFile = open("saves/%s.ent" % name,"rb")
        self.data = pickle.load(saveFile)
        saveFile.close()
