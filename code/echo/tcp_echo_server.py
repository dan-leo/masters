import socket
from time import sleep

print('echo server for NB-IoT stress testing under different radio conditions')

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 5555))
    s.listen(0)
    while True:
        conn, address = s.accept()

        msg = ''
        while True:
            data = conn.recv(1)
            d = data.decode('utf-8')
            msg += d

            if data:
                print(d, end='')
                
            if 's' in msg or 'q' in msg:
                conn.shutdown(1)
                conn.close()
                print()
                if 's' in msg:
                    break
                else:
                    exit()

            if 'd' in d or 'e' in d:
                if 'd' in d:
                    sleep(1)
                conn.send(msg.encode())
                msg = ''
                print()
                break


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass