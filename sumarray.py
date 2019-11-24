def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

def sumArrayV1(arr, total):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if ((arr[i] + arr[j]) == total) and (i != j):
                return (arr[i], arr[j])
    return None

def sumArrayV2(arr, sum):
    arr = [x for x in arr if x < sum]
    end = len(arr) - 1
    i = end
    while ((arr[end] + arr[i] != sum) and (end == i)):
        if i == 0:
            end -= 1
            i = end
        else:
            i -= 1
    #return (arr[i], arr[end])
    return (i, end)

def sumArrayV3(arr, sum):
    found = set()
    for item in arr:
        if (sum - item) in found:
            return True
        else:
            found.add(item)
    return False


print(sumArrayV3([], 8))
