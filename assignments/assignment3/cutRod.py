# cutRod.py
# Brock Smedley 2018
import sys

# naive cutRod algorithm (2^n)
# finds maximum profit of cuts of rod length n based on profit table p[]
def cutRodNaive(p,n):
    #print "n: %d" % n
    #print
    
    if (n <= 0):
        return 0
    
    q = -sys.maxsize-1
    
    for i in range(n):
        q = max(q, p[i % len(p)] + cutRodNaive(p, n-i-1))

    #print "q: %d" % q
    return q


# DP cutRod algorithm (n^2)
def cutRod(p,n):
    r = n*[-sys.maxsize-1]
    return cutRodAux(p,n,r)

def cutRodAux(p,n,r):
    if (r[n-1] >= 0):
        return r[n-1]
    if (n == 0):
        q = 0
    else:
        q = -sys.maxsize-1
        for i in range(n):
            q = max(q, p[i % len(p)] + cutRodAux(p, n-i-1, r))
    r[n-1] = q
    return q


# Bottom-up cutRod algorithm (n^2)?
def cutRodBU(p,n):
    r = n*[0]
    #print r
    #print "n: %d" % n
    for j in range(1,n+1):
        #print "\tj: %d" % j
        q = -sys.maxsize-1
        for i in range(1,j+1):
            #print "i: %d\nj: %d\n" % (i-1, j-1)
            iadj = i % len(p)
            q = max(q, p[iadj-1] + r[j-iadj-1])
        r[j-1] = q
        #print r
    return r[n-1]


def test():
    p = [1,5,8,9,10,17,17,20,24,30]
    n = 10

    print cutRodNaive(p,n)
    print cutRod(p,n)
    print cutRodBU(p,n)

test()
