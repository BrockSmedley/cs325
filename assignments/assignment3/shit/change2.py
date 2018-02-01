# change2.py
# Brock Smedley

def ltrv(r, V):
    for i in range(len(V)):
        if (r < V[i]):
            return true

def change(A,V):
    M = []
    lenv = len(V)
    m = 0
    C = lenv*[0]

    # construct data table
    for i in range(lenv):
        M.append([])
        n = A / V[i]
        print "n: " + str(n)
        for j in range(1,n+1):
            value = j * V[i]
            #print value
            M[i].append(value)

    S = 0
    # construct optimal sum
    for v in range(len(M)):                 # iterare V lo-hi
        for j in range(len(M[v])-1, -1, -1):     # iterate m hi-lo
            if (M[v][j] + S <= A and ltrv(A-S, V[j+1:])):
                S += M[v][j]
                m += j
                C[v] = j
                break

    print "S: %d" % S
    

    for a in M:
        print a
                
            
            

def test():
    A = 142
    V = [100, 7, 3]
    change(A,V)
    


test()
