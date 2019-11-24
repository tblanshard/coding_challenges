def getAlphabet(letters):
    alphabet = set()
    for letter in letters:
        alphabet.add(letter)
    return alphabet

def next_index(c):
    if c == 0:
        return 1
    elif c == 1:
        return 0
    return c

def solve(j):
    alphabet = getAlphabet(j)
    base = max(2, len(alphabet))
    code = {}
    result = 0
    total = len(j)
    for k, i in enumerate(j):
        if i in code:
            new_val = code[i]
        else:
            new_val = next_index(i)
        result += int(((base ^ (total - k)) * new_val))
        code[i]=new_val

print(solve("11001001"))
