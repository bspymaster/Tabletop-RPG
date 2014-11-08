#main.py

#importing
from entity.Entity import *
from entity.Player import *

from grid.Grid import *

from randomNums.Dice import *

#creation
grid = Grid(5,5)

player = Player("Ben",2,health = 10,energy = 3000)

#test grid manipulation
grid.setLocation(2,2,player)

print grid.getLocation(2,2)
print grid.getLocation(4,4)

grid.swapLocation(2,2,4,4)

print grid.getLocation(2,2)
print grid.getLocation(4,4)

#test player data manipulation
for k,v in player.getData().iteritems():
    print "%s = %s" % (k, v)

print "name: " + player.getName()

print "energy: ", player.getKey("energy")
player.removeKey("energy")
try:
    print "energy: ", player.getKey("energy")
except:
    print "getting 'energy' key failed since it was deleted"


#test rolling
rollInfo = Dice.complexDieRoll(["d10","d20","d20"],[10,-3,5])

string = ""
for i in rollInfo[1]:
    string += (str(i) + " + ")

for i in rollInfo[2]:
    string += (str(i) + " + ")

string += " = "

string += str(rollInfo[0])

print string
