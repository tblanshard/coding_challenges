def swapVowels(string):
    vowels = ("a", "e", "i", "o", "u")
    string = list(string)
    rPointer = 0
    fPointer = len(string) - 1
    while fPointer > rPointer:
        if string[rPointer] in vowels:
            while string[fPointer] not in vowels:
                fPointer -= 1
            temp = string[rPointer]
            string[rPointer] = string[fPointer]
            string[fPointer] = temp
            fPointer -= 1
        rPointer += 1
    return "".join(string)

print(swapVowels("apples and oranges"))
print(swapVowels("journal"))
