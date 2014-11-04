#entity.py

class Entity:
    def __init__(self,*args,**kwargs):
        self.data = kwargs
        #PRECONDITION: all *args MUST be dictionaries (used for subclasses)
        for i in args:
            self.getData().update(i)
    
    #adds a new key to the data dictionary
    def setKey(self,key,value):
        self.getData()[key] = value
        return True
    
    #removes the key with the target index and returns the key,value pair as a tuple
    def removeKey(self,key):
        value = self.getKey(key)
        del self.getData()[key]
        return (key,value)
    
    #gets the dynamic dictionary of data stored for the object
    def getData(self):
        return self.data
        """ use this code to printing the items contained in the data dictionary
        for k,v in self.data.iteritems():
            print "%s = %s" % (k, v)
        """
    
    #gets the value at the specific key index
    def getKey(self,key):
        return self.getData()[key]
