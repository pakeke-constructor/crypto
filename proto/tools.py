
import sys
from numba import jit

BYTEORDER = sys.byteorder


@jit(nopython=True)
def to_bytes256(x: int) -> bytes:
    return x.to_bytes(256, byteorder=BYTEORDER)


@jit(nopython=True)
def to_bytes32(x: int) -> bytes:
    return x.to_bytes(32, byteorder=BYTEORDER)


