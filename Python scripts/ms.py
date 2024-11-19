from heapq import merge

def merge_sort(l):
	if len(l) <= 1:
		return l

	middle = len(l) // 2 #integer division by 2
	left = l[:middle] #everything to the left of the middle element
	right = l[middle:] #everything to the right of the middle element

	left = merge_sort(left) #recursively sort the left side
	right = merge_sort(right) #recursively sort the right side

	return list(merge(left, right))

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("merge_sort([1, 2, 3])", setup="from __main__ import merge_sort"))
