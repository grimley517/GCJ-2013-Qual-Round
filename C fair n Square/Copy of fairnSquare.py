import math
import time


def pal(number):
    string = str(number)
    return (string == string [::-1])

def pals(n,m):
    for i in range (n,m):
        if pal(i):
            yield (i)
    
def sqr(n,m):
    start = int(math.ceil(math.sqrt(n)))
    stop = int(math.sqrt(m))+1
    for i in pals(start, stop):
        if pal (i*i):
            yield (i*i)


def analyse(n,m):
    result = 0
    for ans in sqr(n,m):
        result +=1
    return result

start = time.time()
filein = open('C-large-1.in', 'r') 
outfile = open ('sample.out', 'wt')
instances = int(filein.readline())
for i in range (instances):
    l = filein.readline()
    n,m = l.split()
    n = int(n)
    m = int(m)
    answer = analyse(n,m)
    stringStart = str('Case #' + str(i+1) + ': ')
    outfile.write(stringStart + str(answer))
    outfile.write('\n')
filein.close()
outfile.close()
print ('done', time.time() - start)