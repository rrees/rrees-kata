from unittest import TestCase

import sorting

class SortTesting(TestCase):
	def setUp(self):
		self.data = [3, 4, 5, 6, 22, 3, 2, 7, 7, 11, 15, 1, 3, 58]
		self.result = sorted(self.data)

	def test_sorts_should_sort_numbers(self):
		for sort in sorting.sorts:
			self.assertItemsEqual(sort(self.data), self.result)