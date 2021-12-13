import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()
num_of_clients = 0


def five_sort(data):
    print(data)
    final = sorted(data.split(), key=int)
    final = " ".join(final)
    print(final)
    return final


def close(sock):
    sock.shutdown(socket.SHUT_WR)
    print("Connect closed")


# thread function
def threaded(client):
    num_u = []
    count_size = 0
    while True:
        data = client.recv(100)
        if not data:
            print('Close a client connection')
            print_lock.release()
            break

        with open('results.txt', 'a') as file:
            for s in data.split():
                if s.isdigit():
                    count_size += 1
                    num_u.append(int(s))
                    if count_size % 5 == 0:
                        in_file = five_sort(' '.join(map(str, num_u)))
                        num_u = []
                        file.write(str(in_file) + "\n")

        data = five_sort(data.decode('utf-8'))
        client.send(data.encode('utf-8'))

    client.close()


def Main(n):
    first = []
    second = []
    file = open("results.txt", "r+")
    file.truncate(0)
    file.close()
    host = "0.0.0.0"

    global num_of_clients
    port = 9005
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print("socket binded to port", port)
    sock.listen(n)

    while True:
        if num_of_clients < n + 1:
            num_of_clients += 1
            client, addr = sock.accept()
            print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            start_new_thread(threaded, (client,))
        else:
            i = 1
            f = open("results.txt", "r+")
            for line in f.readlines():
                if i % 2 == 0:
                    second.append(line.replace('\n', ""))
                    # print(line)
                else:
                    first.append(line.replace('\n', ""))
                i += 1
            f.close()
            print(', '.join(map(str, first + second)))
            with open('final_results.txt', 'w') as file:
                file.write(', '.join(map(str, first + second)))
            file.close
            close(sock)
            break

    sock.close()


if __name__ == '__main__':
    n = 3
    Main(n)
