from unittest import TestCase
from timeit import Timer

import sorting
import data

class SortTesting(TestCase):
	def setUp(self):
		self.data = data.numbers
		self.result = sorted(self.data)

	def test_sorts_should_sort_numbers(self):
		for sort in sorting.sorts:
			sorted_data = sort(self.data)

		for i in range(len(self.data)):
				assert self.data[i] == self.result[i], "%s: Got %s; expected %s" % (sort, self.data[i], self.result[i])

