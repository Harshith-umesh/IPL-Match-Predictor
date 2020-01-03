#!/usr/bin/env python3
"""reducer.py"""

import sys
curbowl=""
curov=0
curruns=0
curwicks=0
curballs=0
for line in sys.stdin:
    line=line.strip()
    bowl,ov,runs,wicks=line.split(",")
    if(curbowl==bowl):
        if("." in ov):
            ovv,ball=ov.split(".")
            ov=float(ovv)+float(ball)/6
        else:
            ov=int(ov)
        curov+=ov
        curruns+=int(runs)
        curwicks+=int(wicks)
        curballs+=6*int(ovv)+int(ball)
    else:
        avg=sr=econ=0
        if(curbowl):
            if(curov>0):
                if(curwicks>0):
                    avg=curruns/curwicks
                    sr=curballs/curwicks
                econ=curruns/curov
            print("%s,%s,%s,%s,%s,%s,%s,%s"%(curbowl,curruns,curwicks,curov,curballs,avg,sr,econ))
        curbowl=bowl
        if("." in ov):
            ovv,ball=ov.split(".")
            ov=float(ovv)+float(ball)/6
        else:
            ov=int(ov)
        curov=ov
        curruns=int(runs)
        curwicks=int(wicks)
        curballs=6*int(ovv)+int(ball)
if(curbowl==bowl):
    avg=sr=econ=0
    if(curov>0):
        if(curwicks>0):
            avg=curruns/curwicks
            sr=curballs/curwicks
        econ=curruns/curov
    print("%s,%s,%s,%s,%s,%s,%s,%s"%(curbowl,curruns,curwicks,curov,curballs,avg,sr,econ))
