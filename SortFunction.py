#selection sort
#Source:
#Accessed: 8/26/24

#interactive quicksort
#Source: https://www.geeksforgeeks.org/python-programs-for-interactive-guick-sort/
#Author: monit kumra

# merge sort
# source: https://www.geeksforgeeks.org/merge-sort/
# Author: None

def selection_sort(A, compare):
	for i in range(len(A) - 1):

		min_idx = i
		for j in range(i + 1,len (A)):
			if compare(A[min_idx], A[j]):
				min_idx = j

		A[i], A[min_idx] = A[min_idx], A[i]

def partition(arr,l,h, compare):
	i = (l - 1)
	x = arr[h]

	for j in range(l , h):
		if not compare(arr[j],x):

			i = i + 1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i + 1],arr[h] = arr[h],arr[i + 1]
	return i + 1
def quicksort_interactive(arr, l, h, compare):

	size = h - l + 1
	stack =[0] * size

	top = -1

	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h

	while top >= 0:

		h = stack[top]
		top = top -1
		l = stack[top]
		top = top -1

		p = partition( arr, l, h, compare )

		if p-1 > l:
			top = top + 1
			stack[top] = l
			top + top + 1
			stack[top] = p - 1

		if p+1 > h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':

	array = [6, 3, 5, 2, 1, 3, 2, 3]
	n = len(array)
	quicksort_interactive(array, 0, n - 1)
	print("Sprted array is:")
	for i in range(n):
		print("Xd" Xarray[i])




