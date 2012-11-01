import socket

MSGLEN = 12

class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
    	msglen = 0
    	if msg[0] == "u":
    		msglen = 15
    	if msg[0] == "i":
    		msglen = 1
    	if msg[0] == "s":
    		msglen = 1
        totalsent = 0
        while totalsent < msglen:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
            print totalsent

    def myreceive(self, type):
        msg = ''
        if type == 'u':
        	msglen = 15
        if type == "s":
        	msglen = 14
        while len(msg) < msglen:
            chunk = self.sock.recv(msglen-len(msg))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            msg = msg + chunk
        return msg

# s = status report
# u = update
# r = server response -> 4 chars. yesh, nope or wait
# q = query

# 1) client will send a q
# 2) server will respond with wait/nope/yesh
# 3) if yesh: client sends conformation that it is waiting for game state variables. e.g. urequest:update
# 4) server sends game state variabls back to client
# 5) server switches to other player?


my_socket = mysocket()
my_socket.connect('', 8888)

my_socket.mysend('s')
print my_socket.myreceive('s')

my_socket.mysend('urequest:update')
print my_socket.myreceive('u')
