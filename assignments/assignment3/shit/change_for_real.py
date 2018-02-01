# change.py
# Brock Smedley 2018


# M FORMAT
#      i0   i1   i2
# -------------------
# j0 | 02 | 03 | 10
# j1 | 04 | 06 | 20
# j2 | 06 | 09 | 30


def valueSum(C, V):
    s = 0
    for i in range(len(C)):
        s += C[i] * V[i]

    return s


def getV(M):
    V = []
    for i in range(len(M)):
        V.append(M[i][0])
    return V


# start from largest number
def change(M, A, C, i, j):
    x = M[i][j]
    
    # if remainder is smaller than smallest item, x is no good; decrement j
    if (x < M[0][0]):
        if (i >= 0 and j > 0):
            return change(M,A,C,i,j-1)
        
    # but if rem. is larger than smallest item, we have a chance
    else:        
        # check sum first to see if we found a solution
        if (valueSum(C,getV(M)) == A):
            return (C, sum(C)) # m is really just sum(C)

        # recursively fetch sub-solutions
        
        if (i-1 > 0):
            C[i] = j-1
            subC = change(M, A-x, C, 1, len(M[i-1])-1)
            print subC
            C = [x + y for x, y in zip(C, subC[0])]
        else:
            C[i] = C[i] - 1
            i = len(M) - 1
            j = len(M[i])-2         # -2; one for indexing, one for decrementing
            
            return change(M, A, C, i, j)
                    
        if (subC):
            print "subC: %s" % str(subC)
            C = [x + y for x, y in zip(C, subC[0])]
        else:
            exit("error or something")
        return change(M, A, C, i, j)
        



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


def callChange(A,V):
    M = buildTable(A,V)
    C = len(V) * [0]
    i = len(M) - 1
    j = len(M[i]) - 1
    return change(M, A, C, i, j)


def test():
    A = 19
    V = [2, 5, 7]
    
    s = callChange(A, V)

    print s
            
test()
