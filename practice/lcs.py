# lcs.py
# longest common substring


x = 0

def lcs(X,Y):
    m = len(X)
    n = len(Y)

    i = m-1
    j = n-1
    l = []
    global x
    x += 1
    print x
    #print "i: %d"%i
    #print "j: %d"%j
    #print "X: %s"%X
    #print "Y: %s"%Y
    #print

    if (i < 0 or j < 0):
        return []

    if ((i,j) in l):
            return l
    
    if (X[i] == Y[j]):
        lm = [(i,j)]
        lm += lcs(X[:m-1],Y[:n-1])
        #print "lm: %s"%lm
    else:
        l1 = lcs(X[:m-1],Y[:n])
        l2 = lcs(X[:m],Y[:n-1])
        
        if (len(l1) > len(l2)):
            lm = l1
        else:
            lm = l2
        
        
    l += lm
    return l

def test():
    X = [1,5,3,4,8,6,7]
    Y = [5,1,4,5,8,7]

    l = lcs(X,Y)
    print l
    


test()
    
    
