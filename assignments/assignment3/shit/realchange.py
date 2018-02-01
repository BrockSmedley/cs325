# most_change.py
# Brock Smedley



# builds "multiple" cost table from A and V
# V assumed to be taken in lo-hi order
def buildTable(A, V):
    M = []
    for v in V:
        ps = []
        s = 0
        n = A / V[-1]
        for i in range(n+2):
            ps.append(s * v)
            s += 1
        M.append(ps)
    return M


def printTable(M):
    for v in M:
        print v


# computes maximum number of coin things that could be selected
# to add up to A
def traverse(table, C, A):
    cl = len(C)     # local var to bound loops
    s = 0           # running sum; only updates on "i jumps"
    D = []          # renamed C; tracks number of coins used to assemble sum

    # assume table is organized in ascending order in both dimensions
    #while (i >= 0): # iterate over i in descending order
    for i in range(cl-1, -1, -1):
        for j in range(cl+2):
            if (s + table[i][j] < A): # potential component found, continue
                continue
            elif (s + table[i][j] == A):
                D.append((i,j))
                s += table[i][j-1]
                #return (D, get(D))
            else: # too high. jump to next denomination
                D.append((i, j-1))
                s += table[i][j-1]
                break

    return (D, get(D))


def get(D):
    # get sum m from D
    m = 0
    for d in D:
        m += d[1]
    return m


# computes optimal change (like Obama)
def change(A, V):
    table = buildTable(A,V)

    # array of denomination multiple counts
    C = len(V)*[0]
    D = traverse(table, C, A)

    return D    
           

def printChange(change, values, full=False):
    C = change[0] # list of (tuples containing) # of multiples (and indices)
    m = change[1] # m.

    if (full):
        print "C: %s"%C
    print "m: %d"%m

    for t in C:
        print "%dx $%d"%(t[1], values[t[0]])

    
def test():
    A = 35
    V = [3,4,10]

    table = buildTable(A,V)
    #printTable(table)

    ch = change(A,V)
    printChange(ch, V, True)


def getData(fp):
    data = []
    Vs = []
    As = []
    for l in fp:
        data.append(l)

    for d in range(len(data)):
        if (d % 2 == 0):
            Vs.append(data[d].split())
        else:
            As.append(int(data[d]))

        for v in range(len(Vs)):
            for n in range(len(Vs[v])):
                Vs[v][n] = int(n)

    return (As, Vs)
    
def main():
    fp = open("amount.txt", "r")
    data = getData(fp)

    print change(61, [10,4,3])

    As = data[0]
    Vs = data[1]

    
    fp.close()
    fp = open("change.txt", "w")
    for a in range(len(As)):
        sol = change(As[a], Vs[a])
        fp.write(str(sol) + "\n")
    fp.close()

main()
