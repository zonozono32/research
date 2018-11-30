import zmq, msgpack
from zmq_tools import Msg_Receiver
ctx = zmq.Context()
ip = 'localhost' #If you talk to a different machine use its IP.
port = 50020 #The port defaults to 50020 but can be set in the GUI of Pupil Capture.

# open Pupil Remote socket
requester = ctx.socket(zmq.REQ)
requester.connect('tcp://%s:%s'%(ip,port))
requester.send_string('SUB_PORT')
ipc_sub_port = requester.recv_string()

requester = ctx.socket(zmq.REQ)
requester.connect('tcp://%s:%s'%(ip,port))
requester.send_string('PUB_PORT')
ipc_pub_port = requester.recv_string()

# setup message receiver
sub_url = 'tcp://%s:%s'%(ip,ipc_sub_port)
pub_url = 'tcp://%s:%s'%(ip,ipc_pub_port)

receiver = Msg_Receiver(ctx, sub_url, topics=('gaze.2d.01',))

# topic = 'gaze'
# payload = {'topic': topic}
#
# # create and connect PUB socket to IPC
# pub_socket = zmq.Socket(zmq.Context(), zmq.PUB)
# pub_socket.connect(pub_url)
#
# # send payload using custom topic
# pub_socket.send_string(topic, flags=zmq.SNDMORE)
# pub_socket.send(msgpack.dumps(payload, use_bin_type=True))

# wait and print responses
while True:
    # receiver is a Msg_Receiver, that returns a topic/payload tuple on recv()
    topic, payload = receiver.recv()
    print('test')
    print(payload)
