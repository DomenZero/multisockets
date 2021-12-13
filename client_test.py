import argparse
import socket


def argumentsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', help="set list")
    return parser


def Main(message):
    host = '127.0.0.1'
    port = 9005

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        # message sent to server
        s.send(message.encode('utf-8'))

        data = s.recv(1024)
        print('Received from the server :', str(data.decode('utf-8')))
        break
    s.close()


if __name__ == '__main__':
    parser = argumentsParser()
    args = parser.parse_args()
    message = format(args.list)
    Main(message)
