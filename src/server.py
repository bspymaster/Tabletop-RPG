#server.py

from network.ServerHandler import hostProcessor
from SocketServer import ThreadingTCPServer

ip = raw_input("Input host IP: ") or "localhost"
port = raw_input("Input host port: ") or 9000
port = int(port)
print "Running server on %s with port %d..." % (ip,port)

server = ThreadingTCPServer((ip,port),hostProcessor)
server.serve_forever()
