#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
d = {}
for sock in c:
    if c.count(sock) > 1:
        d.update({sock:c.count(sock)})
    

cnt = 0
for key, value in d.iteritems():
    cnt += value/2

print cnt
