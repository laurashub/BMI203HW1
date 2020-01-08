#implement bubble sort

def bubble_sort(li):
	for i in range(len(li)-1):
		for j in range(len(li)-1):
			if li[j] > li[j+1]:
				temp = li[j]
				li[j] = li[j+1]
				li[j+1] = temp
	return li

my_list = [5, 4, 3, 2, 1]
print(bubble_sort(my_list))

#implement insertion sort

#implement quicksort


#test the time complexity of your algorithms as follows

#for sizes of 100, 200 ,300, .. 1000

#generate 100 random vectors

#sort them using your code

#illustrate convincingly that bubble sort is O(n^2) on average
#quicksort is O(n log(n)) on average