import numpy as np

#Count the number of assignments 
#Count the number of conditionals 

def bubblesort(x, count = False):
    """
    For each element e in x, compare it to its right neighbor. If e is larger,
    switch them. Continue until you reach the end of the array or a larger value.
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
    """
    For each element e of x, move through the array until you come to a value 
    that is less than e, or the end of the array, then place e at the new location.
    """
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
    Take an element e at position i to be the pivot, then place all elements less
    than e to the left and all elements greater than e to the right. Repeat on the
    sublists x[0:i] and x[i+1:len(x)] until the list is fully sorted.
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
        
        #ugly adding
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



