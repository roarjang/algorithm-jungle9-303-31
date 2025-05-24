def merge_sort(arr):
	if len(arr) <= 1:
		return arr
		
	# Divde
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	
	# Conquer
	left_sorted = merge_sort(left)
	right_sorted = merge_sort(right)
	
	# Combine
	return merge(left_sorted, right_sorted)
	ㄸ
def merge(left, right):
	result = []
	i, j = 0, 0
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			
	result += left[i:]
	result += right[j:]
	
	return result

print(merge_sort([1, 2, 5, 3, 6]))