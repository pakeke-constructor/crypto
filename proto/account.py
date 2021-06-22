



import secrets

BITS = 384

def makeAccount():
    "generates an account number"
    return secrets.randbits(BITS)












