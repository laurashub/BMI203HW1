import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

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

    assert 1 == 1
    return


