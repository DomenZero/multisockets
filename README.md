# Multisockets

### Task
Create a multi-threaded server that can handle N number of clients.
o In addition, the server contains a buffer of size int = 5.
o This buffer is used to sort the incoming int numbers that clients send to the server.
o All incoming data is written directly to this buffer, no more memory may be allocated
• Server should ensure that the numbers are returned to the clients in a sorted and growing order which the clients in turn print to stdout.
o The numbers from the clients must not be mixed, but each client gets his numbers back in sorted and growing order, 5 at a time.
• Server needs to ensure that all threads that handle the different clients are handled in order, which means that all clients are treated fairly, ie wait the same amount of time.
o First you read the first 5 numbers from Client 1, sort and send back to the same client, then you take the 5 numbers from client 2 sort and send back to Client 2 etc…

Example:
3 clients are connected to the server in the following orders:
• Client A, the client sends 10 numbers in the following sequence 7 5 4 1 9 8 9 7 5 4
• Client B, clients send 10 numbers in the following sequence 10 50 20 10 25 76 89 20 20 50
• Client C, clients send 10 numbers in the following sequence 500 400 400 100 100 700 500 400 100 900
• Results printed to stdout are as follows:
• 1 4 5 7 9, 10 10 20 25 50, 100 100 400 400 500, 4 5 7 8 9, 20 20 50 76 89, 100 400 500 700 900

### Solution
Start server with the Python 
```
# python3 server_code.py
```
Or we could start it in __docker-compose__
Test on the client side
```
# python3 client_test.py --list "7 5 4 1 9 8 9 7 5 4"
# python3 client_test.py --list "10 50 20 10 25 76 89 20 20 50"
# python3 client_test.py --list "500 400 400 100 100 700 500 400 100 900"
```
