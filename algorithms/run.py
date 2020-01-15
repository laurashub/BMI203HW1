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
	#print(x_vals)
	#bubble_time = time_sort(bubblesort)
	#plt.plot(x_vals, bubble_time)
	#plt.show()
	#insert_time = time_sort(insertionsort)
	#quick_time = time_sort(quicksort)


def time_sort(func):
	timing_data = []
	for i in range(100, 1001, 100):
		total_time = 0
		for j in range(100):
			x = np.random.rand(i)
			start_time = timeit.default_timer()
			func(x)
			total_time += timeit.default_timer() - start_time
		timing_data.append(total_time/100)
	return timing_data
		