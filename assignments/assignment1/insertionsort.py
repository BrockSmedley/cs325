# hw1 - insertion sort
# Brock Smedley


def isort(dArr):
    for i in range(1,len(dArr)):
        focus = dArr[i]

        # shift other elements (> focus)
        k = i - 1
        while (k >= 0 and focus < dArr[k]):
            dArr[k + 1] = dArr[k]
            k = k - 1
            
        dArr[k + 1] = focus

    return dArr


# receives array of arrays of data to be sorted
def sortArrays(data):
    for a in range(len(data)):
        data[a] = isort(data[a])
    return data


def readData(filename):
    f = open(filename, "r")
    data = []

    i = 0
    for l in f:
        j = 0
        data.append([])
        for w in l:
            if (j != 0):
                if (w != ' ' and w != '\n'):
                    data[i].append(w)
            j = j + 1
        i = i + 1

    return data


def writeData(data, filename):
    f = open(filename, "w")
    for r in data:
        for i in r:
            f.write(str(i))
            f.write(' ')
        f.write("\n")

    f.close()


def main():
    # read data from file data.txt
    data = readData("data.txt")
    
    # sort it
    print data
    data = sortArrays(data)
    print data
    
    # write output to merge.out
    writeData(data, "insert.out")

main()

# Thank you to Mohit Kumra
