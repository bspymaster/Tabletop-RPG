#main.py

#importing
from entity.Entity import *
from entity.Player import *

from grid.Grid import *

from randomNums.Dice import *

from network.Client import IncomingThread
from socket import socket

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

#client processing
server = socket()

ip = raw_input("Input server IP: ") or "localhost"
port = raw_input("Input server port: ") or 9000
print "Connecting to server on %s with port %d...\n" % (ip,port)

server.connect((ip,port))
username = raw_input("What is your name: ").strip()
server.send(">>ADD %s\n" % username)
incoming = IncomingThread()
incoming.defineServer(server)
incoming.start()

active = True
while active:
    message = raw_input()
    if message.strip():
        if message.rstrip().lower() == "\\quit":
            server.send(">>QUIT\n")
            active = False
        elif message.split()[0].lower() == "\\private":
            colon = message.index(":")
            friend = message[7:colon].strip()
            server.send(">>PRIVATE %s\n%s\n" % (friend,message[colon+1:]))
        else:
            server.send(">>MESSAGE " + message)
