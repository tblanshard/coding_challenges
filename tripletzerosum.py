"""
Find all triplets with zero sum
Given an array of distinct elements. The task is to find triplets in array whose sum is zero.
"""

def isSolution(solutions, p_solution):
    #if the length of the solutions array is greater than 1, then check each of the elements
    if (len(solutions) > 0):
        #iterate through each element in the array
        for item in solutions:
            #sort both of the arrays and compare them
            if ((sorted(item)) == (sorted(p_solution))):
                #if the arrays are identical when sorted, then return false as they are simply a different arrangement of one another
                return False
        #otherwise return true as all of the items in the array have been checked and the potential solution doesn't match any of them
        return True
    #if the array is empty then return true because no solutions have been found previously and so this is our first solution
    else:
        return True

def tripletzerosum(arr):
    #create an array to store the arrays that fit the criteria
    solutions = []
    #create three arrays that iterate through the numbers 0...length of the array passed in
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                #only accept a triplet that adds to 0,
                #doesn't use the same number twice (it can use multiple instances of the same number, but will only use each instance once)
                #hasn't been found before (in a different order)
                if ((arr[i] + arr[j] + arr[k] == 0) and ( i != j and i != k and j != k) and (isSolution(solutions, [arr[i], arr[j], arr[k]]))):
                    #if all of these criteria have been met, it will be added to the solutions array
                    solutions.append([arr[i], arr[j], arr[k]])
                    #print the triplet
                    print("{} {} {}\n".format(arr[i], arr[j], arr[k]))

#tests
tripletzerosum([0, -1, 2, -3, 1])
tripletzerosum([1, -2, 1, 0, 5])
