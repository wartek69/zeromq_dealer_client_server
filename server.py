import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.bind("tcp://0.0.0.0:1234")
while True:
    socket.send_string(f"Random number: {random.random()}")
    #  Wait for next request from client
    try:
        message = socket.recv(zmq.NOBLOCK)
        print(f"Received request: {message}")

    except zmq.Again:
        pass

    #time.sleep (0.001)  

socket.close()
context.term()