#!/usr/bin/env python3
# coding: utf-8

import sys

#get all lines from stdin
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()
    #split the line into items
    items = line.split()
    #output ((i,j),1) in tab-delimited format
    for i in range(len(items)):
        j=i+1
        while(j<len(items)):
            try:
                print('(%s,%s)\t%s' % (items[i], items[j], 1))
                j+=1
            except:
                continue




