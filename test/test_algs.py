import numpy as np
from algorithms import algs

"""
 Some cases to think of: 
 Empty vector 
 Single element vector 
 Duplicated elements 
 Odd vs even length of input vector 
"""

def is_sorted(x):
    return all(x[i] <= x[i+1] for i in range(len(x)-1))

def test_bubblesort():
    assert is_sorted(algs.bubblesort(np.random.rand(5))) #normal odd case
    assert is_sorted(algs.bubblesort(np.random.rand(6))) #normal even case
    assert is_sorted(algs.bubblesort(np.random.rand(1))) #single element vector
    assert is_sorted(algs.bubblesort(np.array([]))) #empty vector
    assert is_sorted(algs.bubblesort(np.array([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))) #duplicated elements

def test_insertionsort():
    assert is_sorted(algs.insertionsort(np.random.rand(5))) #normal odd case
    assert is_sorted(algs.insertionsort(np.random.rand(6))) #normal even case
    assert is_sorted(algs.insertionsort(np.random.rand(1))) #single element vector
    assert is_sorted(algs.insertionsort(np.array([]))) #empty vector
    assert is_sorted(algs.insertionsort(np.array([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))) #duplicated elements

def test_quicksort():
    assert is_sorted(algs.quicksort(np.random.rand(5))) #normal odd case
    assert is_sorted(algs.quicksort(np.random.rand(6))) #normal even case
    assert is_sorted(algs.quicksort(np.random.rand(1))) #single element vector
    assert is_sorted(algs.quicksort(np.array([]))) #empty vector
    assert is_sorted(algs.quicksort(np.array([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))) #duplicated elements
