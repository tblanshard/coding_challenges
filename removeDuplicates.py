def removeDuplicates(string):
    if len(string) > 2:
        output = ""
        letters = set()
        for letter in string:
            if (letter not in letters):
                letters.add(letter)
                output += letter
        return output
    else:
        return string

print(removeDuplicates("aabbccc anthony"))
