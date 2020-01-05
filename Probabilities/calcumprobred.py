#!/usr/bin/env python3
"""reducer.py"""

import sys
curclusters=""
curout=[0,0,0,0,0,0,0]
ctr1=0
ctr2=0
for line in sys.stdin:
    line=line.strip()
    clusters,out,w=line.split(",")
    if(curclusters==clusters):
        i=int(out)
        if(i>5):
            i-=1
        if(int(w)==0):
            ctr+=1
            curout[i]+=1
        ctr1+=1
        curout[6]+=int(w)
    else:
        if(curclusters):
            if(ctr1>20):
                s=""
                for i in range(5):
                    curout[i]/=ctr
                    if(i>0):
                        curout[i]+=curout[i-1]
                    s+=str(curout[i])+","
                s+=str(1.0)+","
                curout[6]/=ctr1
                s+=str(curout[6])
                print("%s,%s"%(curclusters,s))
        curclusters=clusters
        curout=[0,0,0,0,0,0,0]
        i=int(out)
        if(i>5):
            i-=1
        if(int(w)==0):
            ctr=1
            curout[i]=1        
        else:
            ctr=0
            curout[6]=1
        ctr1=1
if(curclusters):
    if(ctr1>20):
        s=""
        for i in range(5):
            curout[i]/=ctr
            if(i>0):
                curout[i]+=curout[i-1]
            s+=str(curout[i])+","
        s+=str(1.0)+","
        curout[6]/=ctr1
        s+=str(curout[6])
        print("%s,%s"%(curclusters,s))
    
