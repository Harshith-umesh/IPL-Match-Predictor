#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split(',')
    line=list(map(lambda x:0 if x=='-' else x.rstrip("*"),line))
    if(len(line))>1:
        #print(name,inn,NO,runs,HS,BF)
        print("%s,%s,%s,%s,%s,%s"%(line[0],line[2],line[3],line[4],line[5],line[7]))
