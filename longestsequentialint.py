def longest_sequence(array):
    array = list(map(int, array))
    longest_sequence = 0
    count = 1

    if len(array) > 0:
        for i, item in enumerate(array):
            if i < (len(array) - 1):
                if (item + 1) == array[i + 1]:
                    count += 1
                else:
                    if longest_sequence < count:
                        longest_sequence = count
                        count = 0
        if count > 0:
            count += 1
            if longest_sequence < count:
                longest_sequence = count
                count = 0

        return (longest_sequence)
    else:
        return -1

array = input()
print(longest_sequence(array))
