import functools

#Q: How do you find the missing number in a given integer array of 1 to 100?

#Potential Q's to ask:
# - is there always a single missing number?
# - if not, what should be returned if there is no missing number?
# - are there any repeated numbers?

def missingNumber(array):
    #the sum of the array should be 50x101=5050
    #therefore the missing number is just 5050-(sum)

    return (5050 - functools.reduce(lambda a,b : a+b, array))

#set up array of numbers 1 to 100
array1to100 = []
for i in range(1, 101):
    array1to100.append(i)

del array1to100[19] #delete 20 from the array
print(missingNumber(array1to100))
