import random
import sys
import time

random.seed(time.time())
f=open("cumprobcc.csv","r")
dcc={}
for line in f.readlines():
    line=line.strip()
    line=line.split(',')
    a=[float(x) for x in line[1:]]
    #for i in range(1,len(a)-1):
    #    a[i]+=a[i-1]
    if(len(line[0])==1):
        line[0]='0'+line[0]
    #a[len(a)-2]=1.0
    dcc[line[0]]=a
f.close()
#print(dcc)

f=open("cumprobpp.csv","r")
dpp={}
for line in f.readlines():
    line=line.strip()
    line=line.split(',')
    a=[float(x) for x in line[1:]]
    #for i in range(1,len(a)-1):
    #    a[i]+=a[i-1]
    #a[len(a)-2]=1.0
    dpp[line[0]]=a
f.close()
#print(dpp)

f=open("BatClustered.csv","r")
dbat={}
for line in f.readlines():
    line=line.strip()
    line=line.split(',')
    dbat[line[0]]=line[1]
f.close()
#print(dbat)

f=open("BowlClustered.csv","r")
dbowl={}
for line in f.readlines():
    line=line.strip()
    line=line.split(',')
    dbowl[line[0]]=line[1]
f.close()
#print(dbowl)

#f=open("teams1.csv","r")
team1=[]
team2=[]
for line in sys.stdin:
    line=line.strip()
    line=line.split(',')
    team1.append(line[0])
    team2.append(line[1])
team1b=team1[-5:]*4
team2b=team2[-5:]*4
#print(team1)
#print(team1)
#print(team1b)
#print(team2b)   

def innings(bat,bowl,t):
    x=0
    b1=bat[x]
    x+=1
    b2=bat[x]
    c1=dbat[b1]
    c2=dbat[b2]
    p1=1
    p2=1
    total=0
    ov=0
    #print(bat)
    #print(bowl)
    #'''
    for i in bowl:
        bc=dbowl[i]
        for q in range(6):            
            d={}
            if(str(b1+'#'+i) in dpp):
                d=dpp
                k=b1+'#'+i
            else:
                k=c1+bc
                d=dcc
            n=0
            p1*=1-d[k][6]
            if(p1<0.5):
                print("%s.%s\t%s\t%s\t%s"%(ov,(q+1),i,b1,'W'))
                if(x==10):
                    print('All out for',total)
                    return total,x
                x+=1
                b1=bat[x]
                c1=dbat[b1]
                p1=1
                continue
            r=random.random()
            for j in d[k][:-1]:
                if(r<j):
                    n=d[k].index(j)
                    break
            if(n>4):
                n+=1
            print("%s.%s\t%s\t%s\t%s"%(ov,(q+1),i,b1,n))            
            if(n%2==0):
                total+=n
            elif(n==1 or n==3):
                total+=n
                temp=b1
                b1=b2
                b2=temp
                temp=c1
                c1=c2
                c2=temp
                temp=p1
                p1=p2
                p2=temp
            if(t>0):
                if(total>t):
                    print("Final score:",total,"for",x-1)
                    return total,x
        temp=b1
        b1=b2
        b2=temp
        temp=c1
        c1=c2
        c2=temp
        temp=p1
        p1=p2
        p2=temp
        ov+=1
    print("Final score:",total,"for",x-1)
    #'''
    return total,x
t1,x1=innings(team1,team2b,-1)
print()
print()
print()
t2,x2=innings(team2,team1b,t1)
if(t1>t2):
    print("Team 1 wins by",(t1-t2),"runs")
elif(t2>t1):
    print("Team 2 wins by",(10-x2+1),"wickets")
else:
    print("Match Tied")
    #'''
