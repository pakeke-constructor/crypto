
'''
TODO get networking done.

also idk if udp packets come with error correction,
you should check that.
(apparently tcp provides EC in header, maybe use hamming
codes or something for udp)

'''

TRUSTED_IPS = [] # List of IP's

TRUSTED_HOLEPUNCHED_SOCKETS = [] # List of trusted holepunched socket connections

def broadcast(data: bytes):
    pass

def recieve(buffer):
    pass


