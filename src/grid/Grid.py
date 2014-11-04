#grid.py

class Grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        #populate grid will null objects
        self.grid = [[None for i in range(0,width)] for j in range(0,height)]
    
    #replaces an object in the grid with None, returns the object removed
    def removeObject(self,x,y):
        return self.setLocation(x,y,None)
    
    #moves the object to end location, deleting current object there and replacing the start location with None, returns the overwritten object
    def moveObject(self,startX,startY,endX,endY):
        removedObject = self.setLocation(endX,endY,self.getLocation(startX,startY))
        self.removeObject(startX,startY)
        return removedObject
    
    #sets the location to the obj and returns what was currently there
    def setLocation(self,x,y,obj):
        removedObject = self.getLocation(x,y)
        self.getGrid()[x][y] = obj
        return removedObject
    
    #switches the objects in the two locations
    def swapLocation(self,X1,Y1,X2,Y2):
        tempObject = self.moveObject(X1,Y1,X2,Y2)
        self.setLocation(X1,Y1,tempObject)
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
