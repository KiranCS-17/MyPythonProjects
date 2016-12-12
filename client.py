#!/bin/python
import zmq
import sys

port = "9999"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)


context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
    
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send ("Hello have a Good Day")
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
