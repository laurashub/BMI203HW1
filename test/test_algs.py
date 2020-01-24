import numpy as np
from algorithms import algs

"""
 Some cases to think of: 
 Empty vector 
 Single element vector 
 Duplicated elements 
 Odd vs even length of input vector 
"""

def test_bubblesort():
    assert _helper(algs.bubblesort)

def test_insertionsort():
    assert _helper(algs.insertionsort)

def test_quicksort():
    assert _helper(algs.quicksort)

basic_tests = ((np.array([5, 4, 3, 2, 1]), np.array([1, 2, 3, 4, 5])), #odd length
        (np.array([6, 5, 4, 3, 2, 1]), np.array([1, 2, 3, 4, 5, 6])), #even length
        (np.array([1]), np.array([1])), #single element
        (np.array([]), np.array([])), #empty
        (np.array([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]), np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))) #duplicate elements

def _helper(func):
    return (all([np.array_equal(func(test),ans) for test, ans in basic_tests]) and #basic tests
           all([_is_sorted(x) for x in map(func, _random_tests())])) #random tests


def _is_sorted(x):
    return all(x[i] <= x[i+1] for i in range(len(x)-1))

def _random_tests():
    return [np.random.rand(x) for x in range(10, 20)] #generate random arrays
