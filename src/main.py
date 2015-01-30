#main.py

#importing
from grid.Grid import Grid

from randomNums.Dice import Dice

from network.Client import IncomingThread, OutgoingThread
from socket import socket
from log.Logging import Logger

#create a logger for the client
log = Logger("client")

#client processing
server = socket()

ip = raw_input("Input server IP: ") or "localhost"
port = raw_input("Input server port: ") or 9000
port = int(port)
print "Connecting to server on %s with port %d...\n" % (ip,port)

ConnectionFailed = False
try:
    server.connect((ip,port))
except:
    print "Connection to the server failed. The program will now quit."
    ConnectionFailed = True

if not ConnectionFailed:
    username = raw_input("What is your name: ").strip()

    server.send(">>ADD %s\n" % username)

    #start thread for recieving messages
    incoming = IncomingThread()
    incoming.defineVariables(server,log)
    incoming.start()

    #start thread for sending messages
    outgoing = OutgoingThread()
    outgoing.defineVariables(server,log)
    outgoing.start()

log.closeLog()
