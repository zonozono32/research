import zmq_tools
import zmq

ctx = zmq.Context()
requester = ctx.socket(zmq.REQ)
requester.connect('tcp://127.0.1.1:50020') #change ip if using remote machine

requester.send_string('SUB_PORT')
ipc_sub_port = requester.recv()

topics_list = (  'notify.eye_process.',
            'notify.player_process.',
            'notify.world_process.')

print('tcp://127.0.1.1:' + ipc_sub_port.decode())
monitor = zmq_tools.Msg_Receiver(ctx, 'tcp://127.0.1.1:%s'%ipc_sub_port.decode(), topics=topics_list)

while True:
    print(monitor.recv())
