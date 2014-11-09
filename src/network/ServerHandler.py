#ServerHandler.py

"""
 Adapted from "Object Oriented Programming in Python,"
 written by Michael H. Goldwasser and David Letscher.
 Used with permission.
"""

from SocketServer import BaseRequestHandler

clientList = dict()

def broadcast(message):
    removalList = []
    for username in clientList:
        try:
            clientList.get(username).send(message)
        except:
            removalList.append(username)
    return removalList

class hostProcessor(BaseRequestHandler):
    def handle(self):
        username = "Unknown"
        brokenClients = []
        active = True
        while active:
            transmission = self.request.recv(1024)
            if transmission:
                command = transmission.split()[0]
                data = transmission[1+len(command):]
                
                #client requests to join
                if command == ">>ADD":
                    username = data.strip()
                    clientList[username] = self.request
                    brokenClients += broadcast(">>NEW %s\n" % username)
                #someone sends a message
                elif command == ">>MESSAGE":
                    brokenClients += broadcast(">>MESSAGE %s\n%s\n" % (username,data))
                #someone sends a private message
                elif command == ">>PRIVATE":
                    rcpt = data.split("\n")[0]
                    if rcpt in clientList:
                        content = data.split("\n")[1]
                        clientList[rcpt].send(">>PRIVATE %s\n%s\n" % (username,content))
                #client requests to quit
                elif command == ">>QUIT":
                    active = False
                    self.request.send(">>GOODBYE\n")
                else:
                    active = False
            
            #remove all broken connections
            for client in brokenClients:
                clientList.pop(client)
                broadcast(">>LEFT %s\n" % client)
            brokenClients = []
            
        self.request.close()
        clientList.pop(username)
        broadcast(">>LEFT %s\n" % username)
