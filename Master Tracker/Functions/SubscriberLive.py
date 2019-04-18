import threading

import zmq

from Data.Datakeepers import DataKeepers


class SubscriberLive(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        idIp1 = DataKeepers.getDataNodeIp(1) + ":" + str(7001)
        idIp1 = DataKeepers.getDataNodeIp(2) + ":" + str(7001)
        self.ips = [idIp]

    def run(self):
        self.sub()


    def sub(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)

        for i in range(len(self.ips)):
         socket.connect("tcp://"+self.ips[i] )
         socket.setsockopt_string(zmq.SUBSCRIBE, str(i + 1))

        for i in range(len(self.ips)):
            strs = str(i)

        while(True):
            s = socket.recv_string()
            DataKeepers.updateTime(int(s))
            print(s)

