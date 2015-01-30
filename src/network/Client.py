#Client.py

"""
 Adapted from "Object Oriented Programming in Python,"
 written by Michael H. Goldwasser and David Letscher.
 Used with permission.
"""

from socket import socket
from threading import Thread

active = True
"""
Used by the client to process data coming in from the server
"""
class IncomingThread(Thread):
    """
    a method meant to be called once to pass various variables into the class from outside the class
    @param socket a socket instance that the current server is running on
    @param Logger a Logger instance that will record events that occur in the Client
    """
    def defineVariables(self,server,log):
        self.server = server
        self.log = log
    """
    a method that will run until the program closes to process data sent from the server
    """
    def run(self):
        global active
        while active:
            try:
                transmission = self.server.recv(1024)
            except:
                transmission = ">>PRIVATE client\nYou have been disconnected from the server. The program will now quit. Please press enter to contrinue.\n>>GOODBYE\n"
                self.log.logEvent("connection dropped")
            lines = transmission.split("\n")[:-1]
            i = 0
            
            while i < len(lines):
                command = lines[i].split()[0]
                param = lines[i][len(command) + 1:]
                #server gives permission to leave
                if command == ">>GOODBYE":
                    active = False
                #new user logs on
                elif command == ">>NEW":
                    print "==>",param, "has joined the chat room"
                #someone else leaves chat room
                elif command == ">>LEFT":
                    print "==>",param, "has left the chat room"
                #someone sends a message
                elif command == ">>MESSAGE":
                    i += 1
                    print "==>",param + ": " + lines[i]
                #someone sends a private message
                elif command == ">>PRIVATE":
                    i += 1
                    print "==>",param + " [private]: " + lines[i]
                i += 1
"""
Used by the client to process data and send that data to the server
"""
class OutgoingThread(Thread):
    """
    a method meant to be called once to pass various variables into the class from outside the class
    @param socket a socket instance that the current server is running on
    @param Logger a Logger instance that will record events that occur in the Client
    """
    def defineVariables(self,server,log):
        self.server = server
        self.log = log
    """
    a method that will run until the program closes to process data submitted by the user and send that data to the server
    """
    def run(self):
        global active
        while active:
            message = raw_input()
            if active: #won't run if server disconnected from client unexpectedly
                if message.strip():
                    if message.rstrip().lower() == "/quit":
                        self.server.send(">>QUIT\n")
                        active = False
                    elif message.split()[0].lower() == "/msg":
                        colon = message.index(":")
                        target = message[5:colon].strip()
                        self.server.send(">>PRIVATE %s\n%s\n" % (target,message[colon+1:]))
                    elif message.split()[0].lower() == "/claimmaster":
                        target = message[13:].strip()
                        self.server.send(">>CLAIMMASTER\n")
                    elif message.split()[0].lower() == "/releasemaster":
                        target = message[15:].strip()
                        self.server.send(">>RELEASEMASTER\n")
                    elif message.split()[0].lower() == "/mute":
                        target = message[6:].strip()
                        self.server.send(">>MUTE %s\n" % target)
                    elif message.split()[0].lower() == "/unmute":
                        target = message[8:].strip()
                        self.server.send(">>UNMUTE %s\n" % target)
                    elif message.split()[0].lower() == "/newgrid":
                        self.server.send(">>NEWGRID %s\n%s\n" %(message.split()[1],message.split()[2]))
                    elif message.split()[0].lower() == "/placeobj":
                        self.server.send(">>PLACEOBJECT %s\n%s\n%s" %(message.split()[1],message.split()[2],message[(len(message.split()[0])+len(message.split()[1])+len(message.split()[2])):]))
                    elif message.split()[0].lower() == "/help":
                        print("COMMAND                FUNCTION\n-------                --------\n/quit                  Quits the server.\n/msg <target>: <msg>   Sends a private message to a target person.\n/claimmaster           Claims yourself for master role.\n/releasemaster         Releases master role for others to take. (master only)\n/mute <target>         Stops a target person from sending global messages. (master only)\n/unmute <target>       Allows a target person to send global messages again. (master only)")
                    elif message.split()[0].lower()[0] == "/":
                        print "That is not a vaild command. Please use /help for more information."
                    else:
                        self.server.send(">>MESSAGE " + message)
