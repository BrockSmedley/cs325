# stoogesort.py
# Brock Smedley 2018

import math
import sys

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


# returns array of data arrays from data file, slices out first number
def readData(filename="data.txt"):
    f = open(filename, "r")
    line = f.readline()
    entries = []
    while (line):
        data = line.split()
        n = int(data.pop(0))
        # convert strings to ints
        for d in range(n):
            data[d] = int(data[d])
            
        entries.append(data)
        line = f.readline()

    f.close()
    print "data successfully read from data.txt!"
    return entries


# write sorted data to file
def writeData(filename, data):
    f = open(filename, "w")
    for d in data:
        for i in d:
            f.write(str(i) + " ")
        f.write("\n")
    f.close()
    print "stooge.out successfully written!"


# test the stoogesort
def test():
    entries = readData()
    sData = []
    for r in entries:
        print "unsorted array: " + str(r)
        n = len(r)
        arr = r
        stooge(arr, 0, n-1)
        sData.append(arr)

    writeData("stooge.out", sData)
    for s in sData:
        print "sorted array: " + str(s)

test()
