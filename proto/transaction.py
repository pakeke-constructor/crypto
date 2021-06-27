
'''

Transactions are classified as a tuple of the
following format:
        ( pub_key, signature, reciever, amount, burn_ratio_guess )
with typing:
        ( uint256, uint256,   uint256,  uint32, float ) )

The reason we don't use a class for this is because numba doesn't JIT
classes easily.
Also tuples can be packed easily

'''


import account
import tools

import secrets
import struct
from numba import jit
from cryptography.hazmat.primitives.asymmetric import ed25519 as ed


@jit(nopython=True)
def pack(public, balance, private=None):
    '''
    
    '''
    return 


@jit(nopython=True)
def unpack(packed):
    '''
    TODO
    unpacks struct into Account object
    '''
    return packed





