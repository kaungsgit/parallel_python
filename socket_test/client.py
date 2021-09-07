import socket
import dill

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
REQUEST_BENCH = "!REQUEST_BENCH"

SERVER = "192.168.1.168"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    print(f'msg length is {msg_length}')
    msg = ''
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length)  # it's always byte type that gets received

        # # this works only for basic types (str, etc...). If data received is serialized, you have to unserialize it.
        # # knowing whether it's a basic string or a serialized object is difficult given they are both type bytes.
        # # better approach would be to serialize everything.
        # # Or, try except if you really want to not serialize basic types.
        # if isinstance(msg, bytes):
        #     msg = msg.decode(FORMAT)

    return msg, msg_length


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(f'[SENT] {message}')

    # print(client.recv(2048).decode(FORMAT))
    received_msg, _ = receive(client)
    print(f'[RECEIVED] {received_msg}')

    return received_msg


if __name__ == '__main__':
    send("Hello World!")
    input()
    send("Hello Everyone!")
    input()
    send("Hello Tim!")
    input()

    bench_pickled = send(REQUEST_BENCH)
    bench = dill.loads(bench_pickled)
    print(bench)

    # input()
    send(DISCONNECT_MESSAGE)
