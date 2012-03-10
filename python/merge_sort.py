from itertools import chain

def merge(list_of_arrays):
	return [i for i in chain.from_iterable(list_of_arrays)]