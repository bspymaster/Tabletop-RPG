#BoardThread.py

from threading import Thread
from Queue import *
from grid.Grid import Grid

import pickle

"""
a class dedicated to processing data related to manipulating the board
"""
class BoardThread(Thread):
    """
    a method meant to be called once to pass various variables into the class from outside the class at startup
    @param Queue a Queue instance used to transport data to other threads existing in the server
    """
    @classmethod
    def defineVariables(self,infoPasser):
        self.queue = infoPasser
        self.grid = Grid(10,10)
    """
    Runs until the program quits and processes all information coming from the client about the board.
    """
    def run(self):
        active = True
        data = None
        while active:
            #get the external data from the queue, if none, indicate so
            try:
                data = self.queue.get()
            except:
                data = None
            
            #process data
            if not data == None:
                if data[0] == ">>NEWGRID":
                    rows = int(data[1].split("\n")[0])
                    columns = int(data[1].split("\n")[1])
                    self.createGrid(rows,columns)
                elif data[0] == ">>PLACEOBJECT":
                    row = int(data[1].split("\n")[0])
                    column = int(data[1].split("\n")[1])
                    rawObj = data[1].split("\n")[2]
                    
                    processedObj = self.processObject(rawObj)
                    objType = processedObj[0].lower()
                    
                    #TODO: Replace later with a lookup in some sort of database for the specified object, allowing for users to make their own objects and information
                    if objType == "rtpc":
                        self.grid.setLocation(row,column,["rtpc",PC_BLUE.png,["data goes here"]]
                    elif objType == "rock":
                        self.grid.setLocation(row,column,["rock",rock.png,["data goes here"]]
                    elif objType == "tree":
                        self.grid.setLocation(row,column,["tree",tree.png,["data goes here"]]
                    elif objType == "wall":
                        self.grid.setLocation(row,column,["wall",wall.png,["data goes here"]]
                    else:
                        pass 
                        
                self.queue.task_done()
    
    """
    creates a new grid object for the gameboard with a specified number or rows and columns
    @param integer the number or rows
    @param integer the number of columns
    """
    def createGrid(self,rows,cols):
        self.grid = Grid(rows,cols)
        print "grid created with ",rows," rows, and ",cols," columns."
    
    """
    takes a string of data and processes it into proper pythonic format for later use
    @param string the data to be processed, in the format "ObjectName(parameters,separated,by,commas)". Please note that object references or pointers won't work
    @return tuple a tuple containing the type of object (as a string) as the first index and the parameters for the object (in a list) as the second parameter
    """
    def processObject(self,data):
        objType = data.split("(")[0]
        information = data[len(objType)+1:len(data)-1] #gets object params and eliminates the parentheses
        information = "[" + information + "]" #appends brackets to the info to make it a readable list
        information  = eval(information) #gives the params in a list format, with proper object types
        print information
        return (objType,information)
    
    """
    saves current object and all data to *.ent in the saves folder. The `*` is replaced by the unique name that each entity has
    @param list a list object to save to a file for later use
    """
    def saveObject(self,obj):
        saveFile = open("saves/%s.ent" % obj[0],"wb")
        pickle.dump(obj,saveFile)
        saveFile.close()

    """
    loads a premade list object with all data
    @param string load's the list object's data from *.ent, replacing `*` with the name of the list object (the first item in the list
    """
    def load(self,name):
        saveFile = open("saves/%s.ent" % name,"rb")
        self.data = pickle.load(saveFile)
        saveFile.close()
