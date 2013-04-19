import os
import math

def findPath(graph,keys,start, nodes, path = []):
    path = path + [start]
    nodes.remove (start)
    if len(nodes) ==0:
        return path
    if not graph.has_key(start):
        return none
    for node in nodes:
        newpath = findPath(graph, node, nodes, path)
        if newpath:
            return newpath
    return none

filein = open ('sample.in', 'r') 
outfile = open ('sample.out', 'wt')
instances = int(filein.readline())

for i in range (instances):
    k,n = filein.readline().split()
    k = int(k)
    keys = []
    for key in range (k):
        keys += filein.readline().split()
    n = int(n)
    chests = {}
    chests[0] = keys
    nodes = [0]
    for ches in range (n):
        chests[ches+1] = filein.readline().split()
        nodes.append(ches+1) 
    answer = findPath(chests, 0, nodes ) 
    stringStart = str('Case #' + str(i+1) + ': ')
    outfile.write(stringStart + str(answer))
    outfile.write('\n')
filein.close()
outfile.close()
