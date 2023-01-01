import socket

IP_ADDRESS = "localhost"  # dummy ip
PORT = 9050

class Connection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create_connection(self):
        print("Connecting to Pluto...\n")
        self.sock.setblocking(False) # setting to non-blocking doesn't wait for connection
        try:
            self.sock.connect((IP_ADDRESS, PORT))
        except ConnectionRefusedError :
            print("Failed to connect to Pluto (connection actively refused by target)")
        except BlockingIOError:
            print("Failed to connect to Pluto (non-blocking socket operation couldnt be done immediately)")
        # handle connection errors here
        self.sock.setblocking(True)
        # set keepalive to true
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        # check for keepalive again
        # check for error again
        print("Pluto Connected\n")

    def write_sock(self, packet):
        self.sock.send(packet)
