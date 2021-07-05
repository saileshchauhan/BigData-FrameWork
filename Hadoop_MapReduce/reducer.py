'''
@Author: Sailesh Chauhan
@Date: 04-07-2021
@Title : This is code for aggregating value for key in hadoop streaming.
'''

import sys

lastkey = None
current = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    try:
        value = int(value)
        if key != lastkey:
            if lastkey is not None:
                print('%s\t%d' % (lastkey, current))
            lastkey = key
            current = 0
        current += 1
    except ValueError:
        pass

if lastkey is not None:
    print('%s\t%d' % (lastkey,current))
