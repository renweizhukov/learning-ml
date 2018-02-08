#!/usr/bin/env python3
"""Generate Recaman's sequence and write it to a text file."""

import sys
from itertools import count, islice

def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count():
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c
        
def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf-8') as f:
        f.writelines("{}\n".format(r)
                     # There is a bug in the code given by tutorial: 
                     # to write 'num' Recaman numbers into the text file,
                     # the stop index should be `num`  instead of `num + 1`.
                     for r in islice(sequence(), num))
        
if __name__ == '__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))
