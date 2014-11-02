#grid.py

class Grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        #populate grid will null objects
        self.grid = [[None for i in range(0,width)] for j in range(0,height)]
    
    #adds an object to the grid at target location, overwriting current object and returns added object for reference. Returns None if object added is Nonetype
    def addObject(self,x,y,obj):
        if not (obj == None):
            self.getGrid()[x][y] = obj
            return obj
        else:
            return None
    
    #replaces an object in the grid with None
    def removeObject(self,x,y):
        self.getGrid()[x][y] = None
        return True
    
    #moves the object to end location, deleting current object there and replacing the start location with None
    def moveObject(self,startX,startY,endX,endY):
        self.addObject(endX,endY,self.getLocation(startX,startY))
        self.removeObject(startX,startY)
        return True
    
    #returns with of grid
    def getWidth(self):
        return self.width
    
    #returns height of grid
    def getHeight(self):
        return self.height
    
    #returns grid
    def getGrid(self):
        return self.grid
    
    #gets object located at target location
    def getLocation(self,x,y):
        return self.getGrid()[x][y]
