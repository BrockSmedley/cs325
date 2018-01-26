# cutRod.py
# Brock Smedley 2018

def cutRod(p,n):
    #print "n: %d" % n
    #print
    
    if (n == 0):
        return 0
    q = -1000000
    for i in range(n):
        q = max(q, p[i] + cutRod(p, n-i-1))

    #print "q: %d" % q
    return q

def test():
    p = [1,5,8,9,10,17,17,20,24,30]
    n = 4
    print cutRod(p,n)

test()
