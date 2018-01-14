# hw1 - mergesort
# Brock Smedley

# receives array with indices representing two halves
# a: start half1
# b: end half1
# c: end half2
def merge(dArray, left, mid, right):
    x = mid - left + 1
    y = right - mid

    # temporary arrays; fill with data from dArray
    leftArr = []
    rightArr = []
    for i in range(x):
        leftArr.append(dArray[left + i])
    for j in range(y):
        rightArr.append(dArray[mid + 1 + j])

    # merge temporary arrays back into original array
    i = 0
    j = 0
    t = left

    while (i < x and j < y):
        if leftArr[i] <= rightArr[j]:
            dArray[t] = leftArr[i]
            i = i + 1
        else:
            dArray[t] = rightArr[j]
            j = j + 1
        t = t + 1

    # get rest of leftArr
    while (i < x):
        dArray[t] = leftArr[i]
        i = i + 1
        t = t + 1

    # get rest of rightArr
    while (j < y):
        dArray[t] = rightArr[j]
        j = j + 1
        t = t + 1


# dArray: array of data to sort
# left: index of left edge
# right: "      " right ""
# returns sorted array
def mergesort(dArray, left, right):
    if (left < right):
        mid = (left + right) / 2

        # sort halves recursively
        mergesort(dArray, left, mid) # left half
        mergesort(dArray, mid + 1, right) # right half
        merge(dArray, left, mid, right) # merge sorted halves

    return dArray

# receives array of arrays of data to be sorted
def sortArrays(data):
    for a in range(len(data)):
        data[a] = mergesort(data[a], 0, len(data[a]) - 1)
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
    writeData(data, "merge.out")

main()

# Thank you to Mohit Kumra
