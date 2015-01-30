#server.py

from network.ServerHandler import HostProcessor
from network.BoardThread import BoardThread
from SocketServer import ThreadingTCPServer
from Queue import *

from log.Logging import Logger

#create a logger for the client
log = Logger("server")
infoPasser = Queue()

ip = raw_input("Input host IP: ") or "localhost"
port = raw_input("Input host port: ") or 9000
port = int(port)
print "Running server on %s with port %d..." % (ip,port)

boardProcessor = BoardThread()
boardProcessor.defineVariables(infoPasser)
boardProcessor.start()

HostProcessor.defineVariables(log,infoPasser)
server = ThreadingTCPServer((ip,port),HostProcessor)
server.serve_forever()
