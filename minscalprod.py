def scalar_product(v1, v2, length):
    total = 0
    for i in range(length):
        total += (v1[i] * v2[i])
    return total

def sort(v):
    if len(v) > 1:
        mid = len(v) // 2
        left = v[:mid]
        right = v[mid:]

        sort(left)
        sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                v[k] = left[i]
                i += 1
            else:
                v[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            v[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            v[k] = right[j]
            j += 1
            k += 1

    return v

def shifted(v1, length, perms, count):
    if len(v1) > 1:
        count += 1
        shifted = []
        for i in range(len(v1)):
            for j in range(i, len(v1) + i):
                shifted.append(v1[j % len(v1)])
            perms.append(shifted)
            shifted(shifted[count:], len(v1) - 1, perms, count)
            shifted = []
    changed = perms
    for shift in changed:
        perms = shifted(shift[:count], length, perms, count)
    return perms

def reverse(v):
    fpointer = len(v) - 1
    rpointer = 0
    while fpointer > rpointer:
        temp = v[fpointer]
        v[fpointer] = v[rpointer]
        v[rpointer] = temp
        fpointer -= 1
        rpointer += 1
    return v

def min_scalar_prod(v1, v2, vector_length):
    return scalar_product(reverse(sort(v1)), sort(v2), vector_length)

def main():
    number_of_cases = int(input())
    outputs = {}
    perms = []
    count = 0
    for case in range(number_of_cases):
        vector_length = int(input())
        v1 = list(map(int, input().split(" ")))
        v2 = list(map(int, input().split(" ")))
        outputs[case + 1] = min_scalar_prod(v1, v2, vector_length)

    for item in outputs:
        print("Case #{}: {}".format(item, outputs[item]))

    print(shifted(v1, vector_length, perms, count))

main()
