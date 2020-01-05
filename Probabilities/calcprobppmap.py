#!/usr/bin/env python3
"""mapper.py"""

import sys
for line in sys.stdin:
	line=line.strip()
	line=line.split(',')
	#print("%s,%s,%s,%s,%s"%(line[4],line[6],line[7],dbat[line[4]],dbowl[line[6]]))
	if(len(line)>9):
	    #continue
	    print("%s,%s,%s"%((line[4]+'#'+line[6]),line[7],1))
	else:
	    print("%s,%s,%s"%((line[4]+'#'+line[6]),line[7],0))
