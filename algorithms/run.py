# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
import matplotlib.gridspec as gridspec
import sys
import math
import matplotlib.pyplot as plt
from .algs import quicksort, insertionsort, bubblesort
from scipy.optimize import curve_fit

def run_stuff():

	functions = [insertionsort, bubblesort, quicksort]
	func_names = ["InsertionSort", "BubbleSort", "QuickSort"]
	timing_data = {}

	ax = [None, None, None]
	fig = plt.figure(constrained_layout=True)
	gs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
	ax[0] = fig.add_subplot(gs[0, :])
	ax[1] = fig.add_subplot(gs[1,0])
	ax[2] = fig.add_subplot(gs[1, 1])
	
	for i, (name, func) in enumerate(zip(func_names, functions)):
		count_stuff(name, func)
		timing_data[name] = time_sort(func)
		x_vals = np.array(range(100, 1001, 100))
		ax[0].plot(x_vals, timing_data[name], label=name)
		if i:
			ax[i].plot(x_vals, timing_data[name], label=name)
			for n, vals in fit_lines(x_vals, timing_data[name]):
				ax[i].plot(x_vals, vals, '--', label=n)
			#complex_func, name, vals = fit_lines(x_vals, timing_data[name])
			#ax[i].plot(x_vals, complex_func(x_vals, *vals), '--', label='Best fit: ' + name)
			ax[i].legend()
			ax[i].set_title(name)
	ax[0].legend()
	ax[0].set_title("All Algorithms")
	plt.savefig('timing_data.png', dpi=200)

def count_stuff(name, func):
	test = np.random.rand(10)
	print("{0}: {1} {2}".format(name, *func(test, count = True)))

def log_relation(x, a):
	return a*(x*np.log(x)) 

def lin_relation(x, a):
	return a*x

def square_relation(x, a):
	return a*(x**2)

def cube_relation(x, a):
	return a*(x**3)

def fit_lines(x_data, y_data):
	complexities = [log_relation, lin_relation, square_relation, cube_relation]
	c_names = ['O(nlog(n))', 'O(n)', 'O(n^2)', 'O(n^3)']
	fit_data = []
	best_residual = float("inf")
	best_vals = []
	best_fit = None

	#get function with the lowest residuals (best fit)
	for i, (c, name) in enumerate(zip(complexities, c_names)):
		vals, covar = curve_fit(c, x_data, y_data)
		fit_data.append(c(x_data, *vals))
		residual = sum(np.square(y_data - c(x_data, *vals)))
		if residual < best_residual:
			best_fit = i
			best_residual = residual
	c_names[best_fit]+=' (Best Fit)'
	return zip(c_names, fit_data)

def time_sort(func):
	timing_data = []
	for i in range(100, 1001, 100):
		assignments, conditionals = 0, 0
		total_time = 0
		for j in range(100):
			x = np.random.rand(i)
			#start_time = timeit.default_timer()
			new_assignments, new_conditionals = func(x, count = True)
			assignments += new_assignments
			conditionals += new_conditionals
			#total_time += timeit.default_timer() - start_time
		timing_data.append((assignments + conditionals)/100)
	return np.array(timing_data)
		