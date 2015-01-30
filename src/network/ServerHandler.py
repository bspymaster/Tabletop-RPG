#ServerHandler.py

"""
 Adapted from "Object Oriented Programming in Python,"
 written by Michael H. Goldwasser and David Letscher.
 Used with permission.
"""

from SocketServer import BaseRequestHandler
from grid.Grid import *
from Queue import *

clientList = dict()
mutedPlayers = []
master = None

"""
used to process and send out a message to all users
@return List a list of all the broken clients
"""
def broadcast(message):
    removalList = []
    for username in clientList:
        try:
            clientList.get(username).send(message)
        except:
            removalList.append(username)
    return removalList
"""
A new instance of this class is created for each client that connects to the server. It processes each client request.
"""
class HostProcessor(BaseRequestHandler):
    """
    a method meant to be called once to pass various variables into the class from outside the class
    @param Logger a Logger instance that will record events that occur in the Server
    @param Queue a Queue instance used to transport data to other threads existing in the server
    """
    @classmethod
    def defineVariables(self,log,infoPasser):
        self.log = log
        self.queue = infoPasser
    """
    Runs until the program quits and processes all information coming from the client.
    """
    def handle(self):
        username = "Unknown"
        active = True
        reUsedNames = 0 #used for generating new names for people who try to log in with an already used name
        while active:
            
            try:
                transmission = self.request.recv(1024)
            except:
                transmission = ">>QUIT\n"
                self.log.logEvent("%s has disconnected unexpectedly" % username)
            
            if transmission:
                command = transmission.split()[0]
                data = transmission[1+len(command):]
                
                ############################
                #GENERAL CLIENT PROCESSING
                ############################
                
                #client requests to join
                if command == ">>ADD":
                    username = data.strip()
                    if (username in clientList) or (username[0:3] == "user") or (len(username) < 2) or (username[0] == " "):
                        failedUsername = username #for logging purposes
                        username = "user%d" % (reUsedNames)
                        reUsedNames += 1
                        self.request.send(">>PRIVATE server\nYou are not allowed to use that name. You are now %s.\n" % username)
                        self.log.logEvent("%s tried to join using the username %s." % (username,failedUsername))
                    clientList[username] = self.request
                    broadcast(">>NEW %s\n" % username)
                    self.log.logEvent("%s joined the chatroom" %username)
                
                #client requests to quit
                elif command == ">>QUIT":
                    global master
                    active = False
                    if master == username:
                        master = None
                        self.log.logEvent("%s released master" % username)
                    #`try:` added for later exception handling when client unexpectedly closed
                    try:
                        self.request.send(">>GOODBYE\n")
                        self.log.logEvent("%s requested to leave" %username)
                    except:
                        pass
                
                ############
                #MESSAGING
                ############
                    
                #someone sends a message
                elif command == ">>MESSAGE":
                    if username not in mutedPlayers:
                        broadcast(">>MESSAGE %s\n%s\n" % (username,data))
                        self.log.logEvent("%s: %s" % (username,data))
                    else:
                        self.request.send(">>PRIVATE server\nYou are not allowed to do that.\n")
                        self.log.logEvent("%s attempted to send '%s'" %(username,data))
                    
                #someone sends a private message
                elif command == ">>PRIVATE":
                    rcpt = data.split("\n")[0]
                    if rcpt in clientList:
                        content = data.split("\n")[1]
                        clientList[rcpt].send(">>PRIVATE %s\n%s\n" % (username,content))
                        self.request.send(">>PRIVATE server\nmessage sent successfully.\n")
                        self.log.logEvent("%s to %s: %s" %(username,rcpt,content))
                    else:
                        self.request.send(">>PRIVATE server\nmessage failed to send.\n")
                
                ########################
                #ADMINISTRATIVE POWERS
                ########################
                
                #claim admin powers
                elif command == ">>CLAIMMASTER":
                    global master
                    if not master:
                        master = username
                        self.request.send(">>PRIVATE server\nYou are now master.\n")
                        self.log.logEvent("%s has claimed master" % master)
                    else:
                        self.request.send(">>PRIVATE server\nMaster is already claimed by %s.\n" % master)
                        self.log.logEvent("%s attempted to claim master when already taken" % username)
                    
                #release admin powers
                elif command == ">>RELEASEMASTER":
                    global master
                    if master == username:
                        master = None
                        self.request.send(">>PRIVATE server\nYou are no longer master.\n")
                        self.log.logEvent("%s released master" %username)
                    else:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                        self.log.logEvent("%s attempted to release master when not master" % username)
                    
                #puts a user to spectate mode
                elif command == ">>MUTE":
                    global master
                    target = data.split("\n")[0]
                    if master != username:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                        self.log.logEvent("%s failed to mute %s when not master" %(username,target))
                    else:
                        try:
                            clientList[target].send(">>PRIVATE server\nYou are being muted.\n")
                            self.request.send(">>PRIVATE server\n%s has been muted.\n" % target)
                            mutedPlayers.append(target)
                            self.log.logEvent("%s muted %s" % (username,target))
                        except:
                            self.request.send(">>PRIVATE server\nFailed to mute %s.\n" % target)
                            self.log.logEvent("%s failed to mute %s" %(username,target))
                    
                #puts a user to spectate mode
                elif command == ">>UNMUTE":
                    global master
                    target = data.split("\n")[0]
                    if master != username:
                        self.request.send(">>PRIVATE server\nYou are not master.\n")
                        self.log.logEvent("%s failed to unmute %s when not master" %(username,target))
                    else:
                        try:
                            mutedPlayers.remove(target)
                            self.request.send(">>PRIVATE server\n%s has been unmuted.\n" % target)
                            clientList[target].send(">>PRIVATE server\nYou are no longer muted.\n")
                            self.log.logEvent("%s unmuted %s" % (username,target))
                        except:
                            self.request.send(">>PRIVATE server\nFailed to unmute %s.\n" % target)
                            self.log.logEvent("%s failed to unmute %s" %(username,target))
                
                ########################
                #BOARD PROCESSING
                ########################
                
                elif command == ">>NEWGRID":
                    self.queue.put((command,data))
                elif command == ">>PLACEOBJECT":
                    self.queue.put((command,data))
                
                else:
                    active = False
            
        self.request.close()
        clientList.pop(username)
        broadcast(">>LEFT %s\n" % username)
        self.log.logEvent("%s left the chatroom" %username)
