#server.py

from network.ServerHandler import HostProcessor
from SocketServer import ThreadingTCPServer

from log.Logging import Logger

#create a logger for the client
log = Logger("server")

ip = raw_input("Input host IP: ") or "localhost"
port = raw_input("Input host port: ") or 9000
port = int(port)
print "Running server on %s with port %d..." % (ip,port)
HostProcessor.defineVariables(log)
server = ThreadingTCPServer((ip,port),HostProcessor)
server.serve_forever()
