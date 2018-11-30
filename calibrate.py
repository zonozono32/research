from time import time, sleep

ctx = zmq.Context()
ip = 'localhost' #If you talk to a different machine use its IP.
port = 50020 #The port defaults to 50020 but can be set in the GUI of Pupil Capture.

requester = ctx.socket(zmq.REQ)
requester.connect('tcp://%s:%s'%(ip,port))
# requester.send_string('SUB_PORT')
# ipc_sub_port = requester.recv_string()

requester.send_string('PUB_PORT')
pub_port = requester.recv_string()
publisher = ctx.socket(zmq.PUB)
publisher.connect('tcp://%s:%s'%(ip, pub_port))
sleep(1) # see Async connect in the paragraphs below
notification = {'subject':'calibration.should_start'}
topic = 'notify.' + notification['subject']
payload = serializer.dumps(notification)
publisher.send_string(topic, flags=zmq.SNDMORE)
publisher.send(payload)
