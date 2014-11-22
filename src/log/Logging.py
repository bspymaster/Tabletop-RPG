#Logging.py

import datetime

class Logger:
    def __init__(self,source):
        if (source != "client") and (source != "server"):
            raise ValueError("Source must be either 'client' or 'server'.")
        date = datetime.datetime.today()
        date = str(date).split(".")[0]
        name = "%s %s" % (source + "_log",date)
        name = name.replace(":",".")
        name += ".log"
        
        self.logFile = open("log/logs/%s/%s" % (source,name), "a")
        
        self.logEvent("logger started")
    
    def getDate(self):
        date = datetime.datetime.today()
        date = str(date).split(".")[0]
        return date
    
    def logEvent(self,event):
        logText = "[" + self.getDate() + "] " + str(event) + "\n"
        self.logFile.write(logText)
    
    def closeLog(self):
        self.logEvent("logger stopped")
        self.logFile.close()
