'''
Write a function that takes in a char *string and converts
series of consecutive identical characters to the number of
consecutive characters and the character itself.
e.g. (aaabbbccccdde => 3a4b5c2d1e)
'''

def find(letters, letter):
    mid = len(letters) // 2
    if (mid >= 1):
        if (letters[mid] == letter):
            return True;
            left = letters[:mid]
            right = letters[mid:]
            if letter > letters[mid]:
                find(left)
            else:
                find(right)


def strtonum(str):
    str = list(str)
    letters = {}
    for letter in str:
        if (find(sorted(list(letters.keys())), letter)):
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    print(letters)

strtonum("aaabbbccccdde")
