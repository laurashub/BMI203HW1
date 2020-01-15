import numpy as np

#Count the number of assignments 
# Count the number of conditionals 

def bubblesort(x, count = False):
    """
    Describe how you are sorting `x`
    """
    assignments = 0
    conditionals = 0
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            conditionals += 1
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
                assignments += 3
    if not count:
        return x
    else:
        return assignments, conditionals

def insertionsort(x, count = False):
    assignments, conditionals = 0, 0
    for i in range(1, len(x)):
        element = x[i]
        j = i - 1
        assignments += 2
        while j > -1 and x[j] > element:
            conditionals += 2
            x[j+1] = x[j]
            j -= 1
            assignments += 2
        x[j+1] = element
        assignments += 1
    if not count:
        return x
    else:
        return assignments, conditionals

def quicksort(x, count = False):
    """
    Describe how you are sorting `x`
    """
    sorted_list, assignments, conditionals = quicksort_helper(x, 0, len(x)-1)
    if not count:
        return sorted_list
    else:
        return assignments, conditionals

def quicksort_helper(x, p, r):
    assignments = 0
    conditionals = 0

    conditionals += 1
    if p < r:
        q, new_assignments, new_conditionals = partition(x, p, r)
        _, new_assignments1, new_conditionals1 = quicksort_helper(x, p, q - 1)
        _, new_assignments2, new_conditionals2 = quicksort_helper(x, q + 1, r)
        assignments += new_assignments
        assignments += new_assignments1
        assignments += new_assignments2

        conditionals += new_conditionals
        conditionals += new_conditionals1
        conditionals += new_conditionals2
    return x, assignments, conditionals

def partition(x, p, r):
    assignments, conditionals = 0, 0


    pivot = x[r] #set pivot to be the last element in the current array
    i = p - 1 #
    assignments += 2
    for j in range(p, r):
        conditionals += 1
        if x[j] <= pivot:
            i += 1
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            assignments += 3
    x[r] = x[i+1]
    x[i+1] = pivot
    assignments += 2
    return i+1, assignments, conditionals



