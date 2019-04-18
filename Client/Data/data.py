import random


class Data:

    global currentFilePath,fileName,userId,ip
    currentFilePath  = ""
    fileName = ""
    userId = 1
    ip = " "
    def __init__(self):
        self.masterIp = ""
        self.masterPorts = [10000,10002,10004]


    def getMasterIp(self):
        return self.masterIp

    def getMasterPort(self):
        random.shuffle(self.masterPorts)  # randomize the array of nodes
        return self.masterPorts[0]

    def getLocalIp(self):
        return "host"

    def getIp(self):
        return ip

