#Client.py

"""
 Adapted from "Object Oriented Programming in Python,"
 written by Michael H. Goldwasser and David Letscher.
 Used with permission.
"""

from socket import socket
from threading import Thread

class IncomingThread(Thread):
    #called once to pass the server instance into the class from outside the class
    def defineServer(self,server):
        self.server = server
    
    def run(self):
        stillChatting = True
        while stillChatting:
            transmission = self.server.recv(1024)
            lines = transmission.split("\n")[:-1]
            i = 0
            
            while i < len(lines):
                command = lines[i].split()[0]
                param = lines[i][len(command) + 1:]
                #server gives permission to leave
                if command == ">>GOODBYE":
                    stillChatting = False
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
