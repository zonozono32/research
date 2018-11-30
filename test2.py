import zmq
from time import sleep,time
from zmq_tools import *

context =  zmq.Context()

#Let the OS choose the IP and PORT
ipc_pub_url = 'tcp://*:*'
ipc_sub_url = 'tcp://*:*'
ipc_push_url = 'tcp://*:*'

# Binding IPC Backbone Sockets to URLs.
# They are used in the threads started below.
# Using them in the main thread is not allowed.
xsub_socket = context.socket(zmq.XSUB)
xsub_socket.bind(ipc_pub_url)
ipc_pub_url = xsub_socket.last_endpoint.decode('utf8').replace("0.0.0.0","127.0.0.1")

xpub_socket = context.socket(zmq.XPUB)
xpub_socket.bind(ipc_sub_url)
ipc_sub_url = xpub_socket.last_endpoint.decode('utf8').replace("0.0.0.0","127.0.0.1")

pull_socket = context.socket(zmq.PULL)
pull_socket.bind(ipc_push_url)
ipc_push_url = pull_socket.last_endpoint.decode('utf8').replace("0.0.0.0","127.0.0.1")

socket = context.socket(zmq.REQ)
# set your ip here
socket.connect('tcp://localhost:50020')
t= time()
socket.send_string('v')
print(socket.recv())
print( 'Round trip command delay:', time()-t)
print( 'If you need continous syncing and/or less latency look at pupil_sync.')
sleep(1)
monitor = Msg_Receiver(context,ipc_sub_url,topics=('notify.eye_process.',)) #change ip if using remote machine


while True:
    print('test')
    print(monitor.recv())
