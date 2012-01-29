from unittest import TestCase
from timeit import Timer

import sorting
import data

def assert_equal(sort, result, target):
	def message(message):
		return "%s: %s %s %s" % (sort, message, result, target)

	assert len(result) == len(target), message("lists are different sizes")
	for i in range(len(target)):
		assert result[i] == target[i], message("values differ")

class SortTesting(TestCase):
	def setUp(self):
		pass

	def test_sorts_should_sort_numbers(self):
		for sort in sorting.sorts:
			input = list(data.numbers)
			sorted_data = sort(input)
			assert_equal(sort, sorted_data, sorted(input))

	def test_similar_values(self):
		for sort in sorting.sorts:
			assert_equal(sort, sort(data.similar_numbers), sorted(data.similar_numbers))
