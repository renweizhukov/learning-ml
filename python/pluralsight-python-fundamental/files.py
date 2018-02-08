#!/usr/bin/env python3

import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        # Don't use print() which will generate extra newlines after each line.
        sys.stdout.write(line)
    f.close()
    
if __name__ == '__main__':
    main(sys.argv[1])
