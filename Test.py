import Protocol
import Connection

packet = Protocol.create_packet(200, [1, 2, 3])
print(packet)

socket = Connection.Connection()
socket.create_connection()

channels = [1500, 1500, 1500, 1500, 1000, 1000, 1000, 1500]
pkt = Protocol.send_req_MSP_SET_RAW_RC(channels)
socket.write_sock(pkt)