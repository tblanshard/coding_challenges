#taken from https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

def reverse_String(string):
    new_string = ""
    for i in range(len(string)):
        new_string += string[len(string) - 1 - i]
    print(new_string)

#reverse_String("Tallie")

def fibs(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return (fibs(n-1) + fibs(n-2))

#print(fibs(7))

def multtable():
    for i in range(1,13):
        for j in range(1,13):
            print("%3d" % (i * j), end=" ")
        print()

#multtable()

def sumfromfile(name):
    total = 0
    f = open(name, "r")
    numbers = f.readlines()
    for number in numbers:
        total += int(number.strip('\n'))
    f.close()
    print(total)

#sumfromfile("test.txt")

def odd_numbers(max):
    for number in range(max + 1):
        if (number % 2 == 1):
            print(number, end=" ")

odd_numbers(99)
