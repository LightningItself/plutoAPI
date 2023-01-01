MSP_SET_RAW_RC = 200


def create_packet(command, payload):
    packet = [ord('$'), ord('M'), ord('<')]
    checksum = 0
    packet_size = (len(payload))
    packet.append(packet_size)
    checksum ^= packet_size
    packet.append(command)
    checksum ^= command
    if packet_size != 0:
        for bit in payload:
            packet.append(bit)
            checksum ^= bit
    packet.append(checksum)
    return bytearray(packet)


def send_req_MSP_SET_RAW_RC(channels):
    rc_signals = []
    index = 0
    for i in range(0, 8):
        rc_signals.append((channels[index] & 0xff))
        rc_signals.append((channels[index] >> 8 & 0xff))
        index += 1
    return create_packet(MSP_SET_RAW_RC, rc_signals)


class Protocol:
    MSP_SET_RAW_RC = 200

    def _init_(self):
        self.input_buffer = []
        self.buffer_index = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.battery = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.acc_z = 0.0

    def read_8(self):
        data = self.input_buffer[self.buffer_index]
        self.buffer_index += 1
        return data
