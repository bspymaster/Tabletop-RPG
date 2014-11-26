#Logging.py

import datetime

"""
Used to record events into a file for future reference
"""
class Logger:
    """
    creates a new Loger instance
    @param string either "client" or "server", used to inform the logger where to save the logfile
    """
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
    """
    gets the current date and time (without milliseconds)
    @return string the date as a string in the format YYYY-MM-DD HH:MM:SS
    """
    def getDate(self):
        date = datetime.datetime.today()
        date = str(date).split(".")[0]
        return date
    """
    creates a new event and writes it down in the logfile in the format `[YYY-MM-DD HH:MM:SS] EVENT`
    @param string a string explaining what event just happened (this writing will be put into the file)
    """
    def logEvent(self,event):
        logText = "[" + self.getDate() + "] " + str(event) + "\n"
        self.logFile.write(logText)
    """
    closes the log (also records in the logfile that the logger was stopped)
    """
    def closeLog(self):
        self.logEvent("logger stopped")
        self.logFile.close()
