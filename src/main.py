#main.py

from entity.Entity import *
from entity.Player import *

from grid.Grid import *

grid = Grid(5,5)

player = Player("Ben",2,health = 10,energy = 3000)

grid.setLocation(2,2,player)

print grid.getLocation(2,2)
print grid.getLocation(4,4)

grid.swapLocation(2,2,4,4)

print grid.getLocation(2,2)
print grid.getLocation(4,4)

for k,v in player.getData().iteritems():
    print "%s = %s" % (k, v)

print player.getName()
