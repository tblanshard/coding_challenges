def find_substrings(sub_str, d = {}):
    for i in range(len(sub_str) + 1):
        for j in range(1, len(sub_str) + 1):
            if i < j:
                sub = sub_str[i:j]
                if sub in list(d.keys()):
                    print(sub)
                    d[sub] = d[sub].append(sub_str)
                else:
                    d[sub] = [sub_str]
    return d

def main():
    str1 = input()
    str2 = input()
    d = find_substrings(str1)
    final = find_substrings(str2, d)
    print(final)

main()
