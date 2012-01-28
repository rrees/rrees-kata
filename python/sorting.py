
def selection_sort(data):
	if len(data) < 2:
		return data

	min = data[0]
	for i in data:
		if i < min:
			min = i

	data.remove(min)
	sorted_data = selection_sort(data)
	sorted_data.insert(0, min)
	return data

sorts = [selection_sort]

