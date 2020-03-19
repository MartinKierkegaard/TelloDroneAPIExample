import socket
import sys
import time


class Drone(object):
    """description of class"""

    def __init__(self, ip,port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        # Create a UDP socket
        self.Host =''
        self.HostPort = 9000
        self.locaddr = (self.Host,self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = ('192.168.10.1', 8889)
        self.sock.bind(self.locaddr)


    def sendMessage(self,TelloMessage):
        print("send message "+ TelloMessage +" end")
        msg = TelloMessage.encode(encoding="utf-8")
        sent = self.sock.sendto(msg,self.tello_address)
        data, server = self.sock.recvfrom(1518)
        #print("returværdi")
        print(data.decode(encoding="utf-8"))
        return "from sendmessage " + TelloMessage + " end "

    def printinfo(self):
        print("Hallo Drone at : "+ self.TelloIp)

    def connect(self):
        print("Connect")
        result = self.sendMessage("command")
        print (result)

    def takeOff(self):
        print("takeOff")
        result = self.sendMessage("takeoff")

    def land(self):
        print("land")
        result = self.sendMessage("land")

    def end(self):
        print("end")
        self.sock.close()
       
    def cw(self,x):
        print("cw")
        r = self.sendMessage("cw "+x)

    def ccw (self,x):
        print("ccw")
        r = self.sendMessage("ccw "+x)
        
    def battery(self):
        r = self.sendMessage("battery?")
        return r



   