import numpy as np

def bubblesort(x):
    """
    Describe how you are sorting `x`
    """
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x

def insertionsort(x):
    for i in range(len(x)):
        element = x[i]
        for j in range(len(x)):
            if x[j] > element:
                x = np.delete(x, i)
                x = np.insert(x, j, [element])
    return x


def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    return(quicksort_helper(x, 0, len(x)-1))


def quicksort_helper(x, p, r):
    if p < r:
        q = partition(x, p, r)
        quicksort_helper(x, p, q - 1)
        quicksort_helper(x, q + 1, r)
    return x

def partition(x, p, r):
    pivot = x[r] #set pivot to be the last element in the current array
    i = p - 1 #
    for j in range(p, r):
        if x[j] <= pivot:
            i += 1
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
    x[r] = x[i+1]
    x[i+1] = pivot
    return i+1



