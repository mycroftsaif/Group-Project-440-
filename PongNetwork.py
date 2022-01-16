import socket

class PongNetwork:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.46.9"
        self.port = 8888
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        #print(self.id)

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print (e)

n = PongNetwork()
print(n.send("hello"))
print(n.send("working"))
