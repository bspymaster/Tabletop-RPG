Tabletop-RPG
============
A basic client to create topdown maps for tabletop RPG players.

Requirements
------------
-Python (preferably 2.7)

Execution
------------
Launch the client by opening `main.py` in Python, and typing in an ip and port that a server is running on.

Launch the server by opening `server.py` in Pyhon, and typing in the ip of the machine and an open port.

For each, leave blank and simply press enter if you wish the server to run the default settings of `localhost` on port `9000`.

Usage
-----------
There are various commands that one can use when using the client:

/help    opens the help dialogue
/claimmaster    sets the user that called this as the master, if none is set
/releasemaster    unsets the user that called this command as master, if he or she is master
/quit    alerts the server that the user is disconnecting (proper way to quit)
/msg <target>: <message>    sends a private message to a target person
/mute <target>    mutes the target user (One must be master to use this)
/unmute <target>    unmutes the target user (One must be master to use this)

To send a global message, simply type in the message and press enter.

To quit the server, it is recommended that all clients are disconnected prior to sutting down the server. Then, simply close the window running the server.
