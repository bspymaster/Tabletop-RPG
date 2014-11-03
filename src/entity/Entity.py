#entity.py

class Entity:
    def __init__(self,*args,**kwargs):
        self.data = kwargs
        #PRECONDITION: all *args MUST be dictionaries (used for subclasses)
        for i in args:
            self.getData().update(i)
    
    #gets the dynamic dictionary of data stored for the object
    def getData(self):
        return self.data
        """ use this code to printing the items contained in the data dictionary
        for k,v in self.data.iteritems():
            print "%s = %s" % (k, v)
        """
