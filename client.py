import zmq
import time

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.DEALER)
socket.connect ("tcp://127.0.0.1:1234")

counter = 0
while True:
    counter+=1
    try:
        socket.send(f"Hello {counter}".encode(), flags=zmq.NOBLOCK)
        #print(f'sending message {counter}')
    except zmq.Again:
        pass
        #print(f"No server detected on message {counter}")
    if counter % 100000 == 0:
        print(f'messages sent: {counter}')
    # Get the reply.
    try:
        message = socket.recv(flags=zmq.NOBLOCK)
        print(f"Received reply {message}")
    except zmq.Again:
        pass

    #time.sleep(0.001)


socket.close()
context.term()