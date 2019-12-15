def shift(arr, start):
    i = len(arr)- 1
    while i >= start:
        arr[i] = arr[i-1]
        i -= 1
    return arr

def mergingArray(n, m):
    npointer = 0
    mpointer = 0
    while mpointer < len(m) and npointer < len(n):
        if n[npointer] == None:
            n[npointer] = m[mpointer]
        while m[mpointer] < n[npointer]:
            n = shift(n, npointer)
            n[npointer] = m[mpointer]
            mpointer += 1
        npointer += 1
    return n

#arr1 = [5,9,15,20,None,None,None,None,None,None]
#arr2 = [1,3,6,8,18,35]
print(mergingArray(arr1, arr2))
