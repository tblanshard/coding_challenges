number_of_lines = int(input())
output = {}
for line in range(number_of_lines):
    words = input().split(" ")
    rpointer = 0
    fpointer = len(words) - 1
    while (fpointer > rpointer):
        temp = words[rpointer]
        words[rpointer] = words[fpointer]
        words[fpointer] = temp
        fpointer -= 1
        rpointer += 1
    output[line + 1] = words
for line in output:
    sentence = " ".join(output[line])
    print("Case #{}: {}".format(line, sentence))
