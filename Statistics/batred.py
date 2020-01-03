#!/usr/bin/env python3
"""reducer.py"""

import sys
curbat=""
curruns=0
curhs=0
curbf=0
curinns=0
curnos=0
avg=0
sr=0
for line in sys.stdin:
    line=line.strip()
    bat,inns,no,runs,hs,bf=line.split(",")
    if(curbat==bat):
        curinns+=int(inns)
        curnos+=int(no)
        curruns+=int(runs)
        curhs=max(curhs,int(hs))
        curbf+=int(bf)
    else:
        avg=sr=0
        if(curbat):
            if(curinns>0):
                if(curinns-curnos>0):
                    avg=curruns/(curinns-curnos)
                else:
                    avg=curruns/curinns
                if(curbf>0):
                    sr=(curruns/curbf)*100
            print("%s,%s,%s,%s,%s,%s,%s"%(curbat,curruns,avg,sr,curhs,curinns,curbf))
        curbat=bat
        curruns=int(runs)
        curhs=int(hs)
        curbf=int(bf)
        curinns=int(inns)
        curnos=int(no)
if(curbat==bat):
    if(curinns>0):
        if(curinns-curnos>0):
            avg=curruns/(curinns-curnos)
        else:
            avg=curruns/curinns
        if(curbf>0):
            sr=(curruns/curbf)*100
    print("%s,%s,%s,%s,%s,%s,%s"%(curbat,curruns,avg,sr,curhs,curinns,curbf))
