

import tools

import sys
import secrets
from numba import jit
from cryptography.hazmat.primitives.asymmetric import ed25519 as ed
from shove import Shove

BITS = 256


@jit(nopython=True)
def pack(public, balance):
    '''
    TODO
    packs Account obj into C struct,
    with format:
        ( pub key, balance )
        ( uint256, uint32 )
    '''
    return 


@jit(nopython=True)
def unpack(packed):
    '''
    TODO
    unpacks struct into Account object
    '''
    return packed



class Account(object):
    accounts = dict()

    def __init__(self, public, private=None):
        if private is not None:
            private = ed.Ed25519PrivateKey.from_private_bytes(
                tools.to_bytes256(private)
            )
            self.isowned = True
        else:
            self.isowned = False
        self.public = ed.Ed25519PublicKey(public)
        self.private = private
        self.balance = 0
        Account.accounts[public] = self.pack()

    @classmethod
    def new():
        '''
        creates and returns an owned account object
        '''
        private = 0
        while private == 0:
            private = secrets.randbits(BITS)
        ed_priv = ed.Ed25519PrivateKey(tools.to_bytes256(private))
        public = ed_priv.public_key()
        return Account(public, private)

    def is_owned(self):
        return self.isowned

    def sign(self, message: bytes):
        '''
        Signs a message from an owned account, and returns the message.
        If the Account is not owned by caller, raises RuntimeError.
        '''
        if not self.owned:
            raise RuntimeError("Attempted to sign a message from an unowned account")
        return self.private.sign(message)

    def is_verified(self, transaction, signature):
        '''
        TODO: this doesnt work lol, need to do more casting and stuff
        '''
        return self.public.verify(transaction, signature)

    def is_private_key(self, potential_priv_key):
        ed_priv = ed.Ed25519PrivateKey(tools.to_bytes256(potential_priv_key))
        return ed_priv.public_key() == self.public_key

    def update(self):
        pass

    def send(self, reciever, amount):
        '''
        sends `amount` of currency to public key account `reciever`.
        '''
        if self.balance < amount:
            return False

    @classmethod
    def test():
        'TODO'
        pass



