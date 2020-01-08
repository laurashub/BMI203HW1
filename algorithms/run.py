# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
import sys
import matplotlib.pyplot as plt
import timeit
from .algs import quicksort, insertionsort, bubblesort

def run_stuff():
	x_vals = list(range(100, 1001, 100))
	print(x_vals)
	time_sort(bubblesort, "Bubble sort")
	time_sort(insertionsort, "Insertion sort")
	time_sort(quicksort, "Quick sort")


def time_sort(func, algo_name):
	timing_data = []
	for i in range(100, 1001, 100):
		total_time = 0
		for j in range(10):
			x = np.random.rand(i)
			start_time = timeit.default_timer()
			func(x)
			total_time += timeit.default_timer() - start_time
			if not (lambda a: np.all(a[:-1] <= a[1:])):
				print("Array not sorted correctly!")
				sys.exit(-1)
		timing_data.append(total_time/10)
	print(timing_data)
		