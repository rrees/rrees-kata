import moka

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

def insertion_sort(data, sorted_data = []):
	if len(data) == 0:
		return sorted_data

	first = data[0]
	rest = data[1:]

	if len(sorted_data) == 0:
		sorted_data.append(data[0])
		return insertion_sort(rest, sorted_data = [first])

	for i in range(len(sorted_data)):
		if first >= sorted_data[i]:
			sorted_data.insert(i, first)
			break

	return insertion_sort(rest, sorted_data = sorted_data)

sorts = [selection_sort, insertion_sort]

