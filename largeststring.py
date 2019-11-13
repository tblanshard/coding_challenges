'''
Compute the longest group of characters in a given string. (e.g. Given "aabbbaabaa" the output should be b3,
as "bbb" is the longest substring consisting of the same character in the string.)
'''

def findLongest(str):
    str = list(str)
    found = False
    count = 0
    longestnum = 0
    longestletter = ''
    for i in range(len(str)):
        if (i != (len(str) - 1)):
            if (str[i] == str[i + 1]):
                found = True;
                count += 1
            else:
                count += 1
                if (count > longestnum):
                    found = False
                    longestnum = count
                    longestletter = str[i]
                count = 0
    print("{}{}".format(longestletter, longestnum))

findLongest("aabbbaabaa")
findLongest("aaaabbbbaabb")
