from itertools import chain

def merge(list_of_arrays, result = None):
	if not result:
		result = []
		list_of_arrays = [sorted(arr) for arr in list_of_arrays]

	if len([a for a in list_of_arrays if len(a) > 0]) == 0:
		return result

	min_head = min([arr[0] for arr in list_of_arrays if len(arr)> 0])

	result.append(min_head)

	new_arrays = []
	head_found = False
	for arr in list_of_arrays:
		if len(arr) == 0:
			continue
		
		if not head_found and arr[0] == min_head:
			new_arrays.append(arr[1:])
			head_found = True
			continue
		
		new_arrays.append(arr)

	return merge(new_arrays, result)

	