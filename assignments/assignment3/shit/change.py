# change.py
# Get minimal amount of exact change for value A in denominations V
# Brock Smedley 2018

# returns true if a - d >= some element in v
def gteDenoms(a, d, v):
    for i in v:
        if (a - d >= i):
            return True
    return False

# A and V should be in integer format (multiply both by 10 until it happens)
def change(A, V):
    lv = len(V)
    C = len(V)*[0]
    m = 0
    i = 0
    
    while (i < lv and A > 0):
        #print "i: %d" % i
        d = V[i]
        if (i + 1 < len(V)):
            dn = V[i+1]
        else:
            dn = 0
        while (A > 0 and (gteDenoms(A,d,V) or (A % d == 0))):
            A -= d
            C[i] += 1
            m += 1
            #print "C: %s" % C
            #print "A: %d" % A
            #print "d: %d" % d
            
        i += 1
    
    if (A == 0):
        return (C,m)
    else:
        print "ERROR -- Cannot make change with given denominations"
        return (None, None)


def change2(A,V):
    maxMultiples = []
    remainders = []
    maxSums = []
    C = len(V)*[0]
    m = 0
    
    for v in V:
        n = A / v
        r = A % v
        maxMultiples.append(n)
        remainders.append(r)
        maxSums.append(n * v)

    i = 0
    for m in maxMultiples:
        total = maxSums[i]
        tRemainder = A - total

        if (tRemainder == 0):
            return 

        # look in V for divisible numbers of the remainder
        j = i+1
        int foundRem = -1
        while (foundRem == -1):
            if (j == len(V)):
                break 
            if (tRemainder % V[j] == 0):
                foundRem = j
                break
            j += 1
            
        if (foundRem >= 0):
            A -= total
            i = foundRem-1
            C[i] = maxMultiples[i]
        else:
            # decrement number of this denomination until next denom. is free to use
            less = (maxMultiples[i] - 1) * V[i]
            k = 2
            while (maxSums[i] - less < V[i+1]):
                # exit condition
                if (k == maxMultiples[i]):
                    maxMultiples[i] = 0 # none of this one
                    maxSums[i] = 0
                    break
                less = (maxMultiples[i] - k) * V[i]
                k += 1

            if (maxMultiples[i] == 0):
                
            
            #i -= 1
            
        i += 1

    print maxMultiples
    print remainders



# returns array of sum values of coins in C
def getTotals(s, V):
    p = []
    for v in range(len(V)):
        if (s[0] == None):
            p.append(None)
        else:
            p.append(s[0][v]*V[v])

    return p


def testLarge(V, f):
    for i in range(V[-1], 201):
        c = f(i,V)
        print "A: %d" % i
        print "Solution: \n%s" % "C: %s\nm: %s" % (c[0], c[1])
        print "Sums(C): %s\n" % getTotals(c, V)


def test():    
    A = 186
    V = [13, 11, 7, 5, 3]

    #print testLarge(V, change2)

    c = change2(A,V)
    print c
    

test()
