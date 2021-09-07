import socket
import threading
import dill
import time

HEADER = 64  # num of digits that can be used to represent of length of message
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
REQUEST_BENCH = "!REQUEST_BENCH"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


class SomeBench:
    def __init__(self):
        self.some_attr = 'some_attr'
        print('Scanning instruments...')
        time.sleep(5)
        print('Scanning completed!')


def send(conn, msg):
    """
    HEADER is 64, meaning the length of object being sent can be as long as 64 digits.
    """

    if isinstance(msg, str):
        message = msg.encode(FORMAT)
    else:
        message = msg  # already bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

    # alternative, use str formatting, :< means left aligned. +msg means add the message at the end.
    # Don't need to send twice anymore
    # f'{len(msg):<{HEADER}}'+msg
    send_length += b' ' * (HEADER - len(send_length))

    conn.send(send_length)
    conn.send(message)
    print(message)

    # print(conn.recv(2048).decode(FORMAT))


def receive(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg = ''
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

    return msg, msg_length


def handle_client(conn, addr, bench):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg, msg_length = receive(conn)
        if msg_length:
            if msg == DISCONNECT_MESSAGE:
                connected = False
            elif msg == REQUEST_BENCH:
                d = {1: "hi", 2: "there"}
                msg_sent = dill.dumps(bench)

                send(conn, msg_sent)

            print(f"[{addr}] {msg}")

            # conn.send("Msg received".encode(FORMAT))

            send(conn, "Msg received")

    conn.close()


def start():
    bench = SomeBench()
    print(bench)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, bench))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == '__main__':
    print("[STARTING] server is starting...")
    start()
