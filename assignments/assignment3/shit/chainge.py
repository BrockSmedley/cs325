#i: for values/rows
#j: for multiples/columns
#e: V[i][j]		# a multiple value
#v: V[i][0]		# a row value (the denomination)


# M FORMAT
#      i0   i1   i2
# -------------------
# j0 | 02 | 03 | 10
# j1 | 04 | 06 | 20
# j2 | 06 | 09 | 30


# recursively builds an optimal sum from table M
# s: sum
# i: row position; current value/price
# j: column position; current multiple
def changeRec(M, A, C, i, j):
    print "CALLED"
    print "A: %d" % A
    print "i: %d" % i
    print "j: %d" % j
        
    # flag for i=0
    if (i < 0):
        r = -1

    add = 0
    h = 0
    v = 0
    
    if (i >= 0 and j >= 0 and i < len(M) and j < len(M[i])):
        h = len(M[i])       # size of column; number of possible multiples
        v = M[i][j]         # price of this column given i & j

        add = C[i] - v

    s = 0
    for z in C:
        s  += z
        
    r = A - (add + s)   # remainer of A minus sum-product and OG sum
    
    print "h: %d" % h
    print "v: %d" % v
    print "r: %d" % r
    print "s: %d" % s
    print "M[0][0]: %d" % M[0][0]

    ### BASE CASES BOIIIIIIIIIIII
    # remainder is 0 so we found a solution; return
    if (r == 0):
        C[i] = j

        m = 0
        for lol in C:
            m += lol
        
        return (C, m)
    # sum-product too big to make exact change; decrement column or row
    elif (r > M[0][0]): # check against smallest number
        if (j < 0):
            i -= 1
            if (i < 0):
                return (None, None)
            j = len(M[i])-1
        return changeRec(M, A, C, i, j-1)
            
    else:
        # found a candidate; add to sum and recurse (decrement) to next coin
        print "i: %d" % i
        print "j: %d" % j
        C[i] = j+1      # add 1 b/c j is an index but we want its 1-indexed val.
        i -= 1
        if (i >= 0):
            j = len(M[i]) - 1
        else:
            return changeRec(M,A,C,i,j)
        print "i: %d" % i
        print "j: %d" % j

        print "from idk"
        return changeRec(M,A,C,i,j)



# builds multiple-cost table from A and V
# V assumed to be taken in lo-hi order
def buildTable(A, V):
    M = []
    for v in V:
        ps = []
        s = 1
        while (s*v < A):
            ps.append(s * v)
            s += 1
        M.append(ps)

    return M


def printTable(M):
    for v in M:
        print v


def test():
    A = 19
    V = [2,5]
    M = buildTable(A, V)
    printTable(M)

    C = len(V)*[0]

    # indices to navigate table
    i = len(V) - 1
    j = len(M[i]) - 1

    s = changeRec(M, A, C, i, j)

    print s
            
test()
