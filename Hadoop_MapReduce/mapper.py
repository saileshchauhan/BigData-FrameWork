'''
@Author: Sailesh Chauhan
@Date: 04-07-2021
@Title : This is code for creating key value pair for hadoop streaming.
'''
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print('%s\t%s' % (word, 1))
