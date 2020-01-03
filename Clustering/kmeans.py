from __future__ import print_function

import re
import sys
from operator import add
import numpy as np

from pyspark.sql import SparkSession

def parseNeigh(lines):
    parts = re.split(r',', lines)
    return np.array([parts[0],parts[1],parts[2],parts[3]])

def closestPoint(pq, centers):
    p=pq[1:].astype('float64')
    #print("1")
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = np.sum((p - centers[i]) ** 2)
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    #return p
    return bestIndex

def centro(x):
    #print(type(x))
    l=0
    for i in x:
        l=len(i)-1
        break
    a=np.zeros(l)
    c=0
    for k in x:
        c+=1
        i=k[1:].astype('float64')
        for j in range(l):
            a[j]+=i[j]
    for i in range(l):
        a[i]/=c
    return a

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: kmeans <file> <k> <convergeDist>", file=sys.stderr)
        sys.exit(-1)

    # Initialize the spark context.
    spark = SparkSession\
        .builder\
        .appName("K-Means")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    data = lines.map(lambda lin: parseNeigh(lin)).cache()
    K=int(sys.argv[2])
    convergeDist = float(sys.argv[3])
    kPoints=data.takeSample(False,K,1)
    z=[]
    for i in kPoints:
        z.append([float(k) for k in i[1:]])
    for i in range(50):
        clcs=data.map(lambda x: (closestPoint(x,z),x)).groupByKey()
        '''for x,y in clcs.collect():
            print(x,y)
        '''
        abc=clcs.map(lambda x:(x[0],centro(x[1])))
        
        '''for x,y in abc.collect():
            print(x,y)'''
        for x,y in abc.collect():
            z[x]=y
    for i,j in clcs.collect():
        for x in j:
            print(x[0],",",i,sep="")
    spark.stop()
