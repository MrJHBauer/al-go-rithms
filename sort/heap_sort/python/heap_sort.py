# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

def test():
    test1 = test3 = [12, 11, 13, 5, 6, 7]
    test2 = test4 = [10,67,2,998,23,56,32,21,91,21,22]
    heapSort(test1)
    heapSort(test2)
    assert (sorted(test3) == test1)
    assert (sorted(test4) == test2)

if __name__=="__main__":
    test()
