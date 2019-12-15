def localmax(array):
    maximas = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            maximas.append(array[i])
    return maximas

print(localmax([1,3,5,4,7,10,6]))
