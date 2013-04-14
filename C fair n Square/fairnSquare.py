import math
import time


def pal(number):
    string = str(number)
    return (string == string [::-1])

def pals(m):
    i=0
    while i < m:
        if pal(i):
            yield (i)
        i+=1
    
def sqr(n,m):
    start = int(math.ceil(math.sqrt(n)))
    stop = int(math.sqrt(m))+1
    for i in pals(stop):
        if pal (i*i):
            yield (i*i)


def analyse(n,m):
    result = []
    for ans in sqr(n,m):
        result.append(ans)
    return result
start = time.time()

FSNs = analyse(0,10**20)


#filein = open('C-large-1.in', 'r') 
#outfile = open ('sample.out', 'wt')
#instances = int(filein.readline())
#for i in range (instances):
#    l = filein.readline()
#    n,m = l.split()
#    n = int(n)
#    m = int(m)
#    answer = analyse(n,m)
#    stringStart = str('Case #' + str(i+1) + ': ')
#    outfile.write(stringStart + str(answer))
#    outfile.write('\n')
#filein.close()
#outfile.close()
print (FSNs)
print ('done', time.time() - start)