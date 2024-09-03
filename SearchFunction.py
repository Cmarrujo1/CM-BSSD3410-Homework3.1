#Source: https://www.geeksforgeeks.org/binary-search/
#Accesed: 8/26/24
#Author: None

def binary_search_sub(arr, l, r, x):

	mid = 0
	while l <= r:

		mid = l + (r - l) // 2

		if arr[mid] == x:
			return mid

		elif arr[mid] < x:
			l = mid + 1

		else:
			r = mid - 1

	return mid

if __name__ == "__main__":
	arr = [2, 3, 4, 10, 40]
	x = 10

	result = binary_search_sub(arr, 0, len(arr) - 1, x)
	if result != -1:
		print("Element is present at index", result)

	else:
		print("Element is not present in array")