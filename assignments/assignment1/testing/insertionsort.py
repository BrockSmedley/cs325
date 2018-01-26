# hw1 - insertion sort
# Brock Smedley

from random import *
import time


def isort(dArr):
    for i in range(1,len(dArr)):
        focus = dArr[i]

        # shift other elements (> focus)
        k = i - 1
        while (k >= 0 and focus < dArr[k]):
            dArr[k + 1] = dArr[k]
            k = k - 1
            
        dArr[k + 1] = focus

    return dArr


# generates random data to be sorted
def readData(n):
    arr = []
    for i in range(n):
        arr.append(randint(0,10000))

    return arr


def main():
    # generate data
    sizes = [1000, 2000, 5000, 10000, 25000, 50000]
    for s in sizes:
        data = readData(s)
        
        # sort it
        startTime = time.time()
        data = isort(data)
        endTime = time.time()

        print ("running time %s items: %s s" % (s, (endTime - startTime)))


main()

# Thank you to Mohit Kumra
