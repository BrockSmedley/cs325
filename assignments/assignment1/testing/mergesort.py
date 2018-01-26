# hw1 - merge sort
# Brock Smedley

from random import *
import time

# receives array with indices representing two halves
# a: start half1
# b: end half1
# c: end half2
def merge(dArray, left, mid, right):
    x = mid - left + 1
    y = right - mid

    # temporary arrays; fill with data from dArray
    leftArr = []
    rightArr = []
    for i in range(x):
        leftArr.append(dArray[left + i])
    for j in range(y):
        rightArr.append(dArray[mid + 1 + j])

    # merge temporary arrays back into original array
    i = 0
    j = 0
    t = left

    # sort
    while (i < x and j < y):
        if leftArr[i] <= rightArr[j]:
            dArray[t] = leftArr[i]
            i = i + 1
        else:
            dArray[t] = rightArr[j]
            j = j + 1
        t = t + 1

    # get rest of leftArr
    while (i < x):
        dArray[t] = leftArr[i]
        i = i + 1
        t = t + 1

    # get rest of rightArr
    while (j < y):
        dArray[t] = rightArr[j]
        j = j + 1
        t = t + 1


# dArray: array of data to sort
# left: index of left edge
# right: "      " right ""
# returns sorted array
def mergesort(dArray, left, right):
    if (left < right):
        mid = (left + right) / 2

        # sort halves recursively
        mergesort(dArray, left, mid) # left half
        mergesort(dArray, mid + 1, right) # right half
        merge(dArray, left, mid, right) # merge sorted halves

    return dArray
        

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
        data = mergesort(data, 0, len(data)-1)
        endTime = time.time()

        print ("running time %s items: %s s" % (s, (endTime - startTime)))


main()

# Thank you to Mohit Kumra
