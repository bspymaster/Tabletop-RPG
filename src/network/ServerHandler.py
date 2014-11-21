#ServerHandler.py

"""
 Adapted from "Object Oriented Programming in Python,"
 written by Michael H. Goldwasser and David Letscher.
 Used with permission.
"""

from SocketServer import BaseRequestHandler

clientList = dict()
mutedPlayers = []
master = None

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
        active = True
        while active:
            
            try:
                transmission = self.request.recv(1024)
            except:
                transmission = ">>QUIT\n"
            
            if transmission:
                command = transmission.split()[0]
                data = transmission[1+len(command):]
                
                #client requests to join
                if command == ">>ADD":
                    username = data.strip()
                    if username in clientList:
                        username = "user %d" % (len(clientList) + 1)
                        self.request.send(">>PRIVATE server\nThis person is already logged on. You are now %s.\n" % username)
                    clientList[username] = self.request
                    broadcast(">>NEW %s\n" % username)
                    
                #someone sends a message
                elif command == ">>MESSAGE":
                    if username not in mutedPlayers:
                        broadcast(">>MESSAGE %s\n%s\n" % (username,data))
                    else:
                        self.request.send(">>PRIVATE server\nYou are not allowed to do that.\n")
                    
                #someone sends a private message
                elif command == ">>PRIVATE":
                    rcpt = data.split("\n")[0]
                    if rcpt in clientList:
                        content = data.split("\n")[1]
                        clientList[rcpt].send(">>PRIVATE %s\n%s\n" % (username,content))
                        
                #claim admin powers
                elif command == ">>CLAIMMASTER":
                    global master
                    if not master:
                        master = username
                        self.request.send(">>PRIVATE server\nYou are now master.\n")
                    else:
                        self.request.send(">>PRIVATE server\nMaster is already claimed by %s.\n" % master)
                
                #release admin powers
                elif command == ">>RELEASEMASTER":
                    global master
                    if master == username:
                        master = None
                        self.request.send(">>PRIVATE server\nYou are no longer master.\n")
                    else:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                
                #puts a user to spectate mode
                elif command == ">>MUTE":
                    global master
                    target = data.split("\n")[0]
                    if master != username:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                    else:
                        try:
                            clientList[target].send(">>PRIVATE server\nYou are being muted.\n")
                            self.request.send(">>PRIVATE server\n%s has been muted.\n" % target)
                            mutedPlayers.append(target)
                        except:
                            self.request.send(">>PRIVATE server\nFailed to mute %s.\n" % target)
                
                #puts a user to spectate mode
                elif command == ">>UNMUTE":
                    global master
                    target = data.split("\n")[0]
                    if master != username:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                    else:
                        try:
                            mutedPlayers.remove(target)
                            self.request.send(">>PRIVATE server\n%s has been unmuted.\n" % target)
                            clientList[target].send(">>PRIVATE server\nYou are no longer muted.\n")
                        except:
                            self.request.send(">>PRIVATE server\nFailed to unmute %s.\n" % target)
                
                #client requests to quit
                elif command == ">>QUIT":
                    global master
                    active = False
                    if master == username:
                        master = None
                    #`try:` added for later exception handling when client unexpectedly closed
                    try:
                        self.request.send(">>GOODBYE\n")
                    except:
                        pass
                    
                else:
                    active = False
            
        self.request.close()
        clientList.pop(username)
        broadcast(">>LEFT %s\n" % username)
