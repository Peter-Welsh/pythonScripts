def insertion_sort(l):
	for i in xrange(1, len(l)):
		j = i-1 
		key = l[i]
		while (l[j] > key) and (j >= 0):
			l[j+1] = l[j]
			j -= 1
		l[j+1] = key

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("insertion_sort([10])", setup="from __main__ import insertion_sort"))