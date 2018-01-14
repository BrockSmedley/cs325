from random import *

z = 0

def mergesort(a):
    # some O(n logn) (or better) sorting algorithm
    return sorted(a)

def hasSum(S,x):
    S = mergesort(S)
    return checkSum(S,x,-1)


def checkSum(S,x,h):
    global z
    z = z + 1
    first = S[0]
    last = S[-1]
    _sum = first + last

    # base case 1: out of elements
    if (len(S) == 2):
        if (_sum == x):
            return True
        else:
            return False

    # base case 2: found a pair
    if (_sum == x):
        return True
    elif (_sum < x):
        h = S.pop(0)
    elif (_sum > x):
        if (h != -1):
            S.insert(0,h)
        S.pop(-1)
        h = -1
    return checkSum(S,x,h)


def test():
    S = []

    for i in range(1,100,2):
        S.append(1)
    #x = S[len(S)/2] + 0.5
    x = 1
    print x
    #print sorted(S)
    print S
    print hasSum(S,x)

    print "array size: " + str(len(S))
    print "iterations: " + str(z)

test()
