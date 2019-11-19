def alien(alphabet, options, string):
    results = []
    for word in alphabet:
        count = 0
        valid = True
        for i in range(len(word)):
            if (word[i] == string[i] and valid):
                valid = True
            else:
                if (string[i] == "." and valid):
                    if word[i] in options[count]:
                        valid = True
                        count += 1
                    else:
                        valid = False
                else:
                    valid = False
        if valid:
            results.append(word)
    return len(results)

inputs = list(map(int, input().split(" ")))
length_word = inputs[0]
length_alphabet = inputs[1]
number_cases = inputs[2]
alphabet = []
results = {}
for word in range(length_alphabet):
    alphabet.append(input())
for case in range(number_cases):
    options = []
    string = ""
    substring = ""
    word = input()
    flag = False
    for i, c in enumerate(word):
        if c != '(' and c != ')':
            if flag:
                substring += c
            else:
                string += c
        elif (c == '('):
            flag = True
            string += '.'
        else:
            options.append(substring)
            substring = ""
            flag = False

    results[case + 1] = alien(alphabet, options, string)

for result in results:
    print("Case #{}: {}".format(result, results[result]))
