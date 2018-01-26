# stoogesort_test.py
# Brock Smedley 2018

import math
import sys
from random import randint
import timeit

# modifies array in place
def stooge(arr, l, r):
    if (l >= r):
        return

    if (arr[l] > arr[r]):
        temp = arr[r]
        arr[r] = arr[l]
        arr[l] = temp

    if ((r - l + 1) > 2):
        m = int(math.ceil((r - l + 1) / 3.0))
        stooge(arr, l, r-m)
        stooge(arr, l+m, r)
        stooge(arr, l, r-m)


# returns array[n] of random data
def readData(n):
    data = []
    for i in range(n):
        data.append(randint(1,1000))

    #print "unsorted data: \t" + str(data)
    return data


# accepts list of run-times, writes each into a csv
def writeData(data):
    f = open("data.out", "w")
    f.write("n \t time \n")
    i = 0
    for d in data:
        dw = str(d[1])
        n = str(d[0])
        f.write("%s \t %s"%(str(n) ,str(dw)))
        if (i < len(data)-1):
            f.write("\n")
        i += 1


# test the stoogesort
def test():
    m = 1600
    r = 20
    w = m / r
    times = []
    for i in range(r):
        n = (i+1)*w
        #print "n: " + str(n)
        data = readData(n)
        t = timeit.default_timer()
        stooge(data, 0, n-1)
        d = timeit.default_timer() - t
        times.append([n, d])
        #print ("running time: %s seconds" % str(d))
    writeData(times)
    #print "sorted array: \t" + str(data)

test()
