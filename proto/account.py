



import secrets
from cryptography.hazmat.primitives.asymmetric import ed25519 as ed



BITS = 256

class Account(object):
    accounts = dict()

    def __init__(self, public, private=None):
        if private is not None:
            private = ed.Ed25519PrivateKey.from_private_bytes(bin(private))
            self.isowned = True
        else:
            self.isowned = False
        self.public = ed.Ed25519PublicKey(bin(public))
        self.private = private
        self.balance = 0
        Account.accounts[public] = self

    @classmethod
    def new():
        '''
        creates and returns an owned account object
        '''
        private = secrets.randbits(BITS)
        public = private.public_key()
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

    def is_verified(self, message):
        return self.public.verify(message)

    def update(self):
        pass

    def send(account, amount):
        '''

        '''
        if self.balance < amount:
            return False
        


    @classmethod
    def test():
        'TODO'
        pass













