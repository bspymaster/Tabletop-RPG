#grid.py

class Grid:
    """
    Creates a new instance of a Grid object for putting objects on
    @param integer the number of rows of the grid
    @param integer the number of columns of the grid
    """
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        
        #populate grid will null objects
        self.grid = [[None for i in range(0,rows)] for j in range(0,cols)]
    
    """
    replaces an object in the grid with None, returns the object removed
    @param integer the row number of the object to remove
    @param integer the column number of the object to remove
    @return object the object removed
    """
    def removeObject(self,x,y):
        return self.setLocation(x,y,None)
    
    """
    moves the object to end location, deleting current object there and replacing the start location with None
    @param integer the row of the object being moved
    @param integer the column of the object being moved
    @param integer the row to move the object to
    @param integer the column to move the object to
    @return object the overwritten object
    """
    def moveObject(self,startX,startY,endX,endY):
        removedObject = self.setLocation(endX,endY,self.getLocation(startX,startY))
        self.removeObject(startX,startY)
        return removedObject
    
    """
    sets the location to the obj
    @param integer the row to set
    @param integer the column to set
    @param object the object to set at the desired row and column
    @return object the object that was there before the location was set
    """
    def setLocation(self,x,y,obj):
        removedObject = self.getLocation(x,y)
        self.getGrid()[x][y] = obj
        return removedObject
    
    """
    switches the objects in the two locations
    @param integer the row of the first location to swap
    @param integer the column of the first location to swap
    @param integer the row of the second location to swap
    @param integer the column of the second location to swap
    @return boolean always returns true
    """
    def swapLocation(self,X1,Y1,X2,Y2):
        tempObject = self.moveObject(X1,Y1,X2,Y2)
        self.setLocation(X1,Y1,tempObject)
        return True
    
    """
    gets the number of rows of the grid
    @return integer the number of rows in the grid
    """
    def getRows(self):
        return self.rows
    
    """
    gets the number of columns of the grid
    @return integer the number of columns in the grid
    """
    def getCols(self):
        return self.cols
    
    """
    gets the grid object
    @return Grid the grid object
    """
    def getGrid(self):
        return self.grid
    
    """
    gets the object located at the target location
    @param integer the row of the desired location
    @param integer the column of the desired location
    @return object the object located at the desired row and column
    """
    def getLocation(self,x,y):
        return self.getGrid()[x][y]
