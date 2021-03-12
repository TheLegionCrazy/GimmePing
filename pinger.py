import json
import socket
import struct


def write_varint(number):
    data = b''

    while True:
        byte = number & 0x7F
        number >>= 7
        data += struct.pack('B', byte | (0x80 if number > 0 else 0))

        if number == 0:
            break

    return data


def serialize_data(data):
    if type(data) is str:
        data = data.encode('utf8')
        return write_varint(len(data)) + data
    elif type(data) is int:
        return struct.pack('H', data)
    elif type(data) is float:
        return struct.pack('Q', int(data))
    else:
        return data


def write_packet(connection, *args):
    data = b''

    for arg in args:
        data += serialize_data(arg)

    connection.send(write_varint(len(data)) + data)


def read_varint(connection):
    number = 0
    for i in range(8):
        data = connection.recv(1)
        if len(data) == 0:
            break

        byte = ord(data)
        number |= (byte & 0x7F) << 7 * i

        if not byte & 0x80:
            break

    return number


def read_packet(connection):
    packet_size = read_varint(connection)
    packet_id = read_varint(connection)

    if packet_id == -1:
        return None

    data_length = read_varint(connection)
    if data_length < 1:
        return None

    data = b''
    while len(data) < data_length:
        data += connection.recv(data_length)

    return data


# See https://wiki.vg/Server_List_Ping
def ping(**kwargs):
    host = kwargs['host']
    port = kwargs.get('port', 25565)
    timeout = kwargs.get('timeout', 0.75)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        connection.settimeout(timeout)
        connection.connect((host, port))

        # Send handshake: packet id 0x00, server address, server port, next state (1 = status, 2 = login)
        write_packet(connection, b'\x00\x00', host, port, b'\x01')

        # Request status: packet id 0x00
        write_packet(connection, b'\x00')

        # Read status packet: packet size, packet id, data length + data
        data = read_packet(connection)

    if not data:
        return None

    return json.loads(data.decode('utf8'))
