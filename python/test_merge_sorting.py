
from unittest import TestCase

import merge_sort

class MultipleMergeSorting(TestCase):
	def test_basic_sort_should_work(self):
		data = [
			[5, 4, 3],
			[7, 3, 3, 6],
			[1, 9, 8, 1],
			[4, 6, 0]
			]
		result = merge_sort.merge(data)

		def concat(a, b):
			a.extend(b)
			return a

		expected_result = sorted(reduce(concat, data, []))
		print expected_result

		for i, value in enumerate(expected_result):
			print i, value
			assert result[i] == value, "Expected %s, got %s: %s" % (value, result[i], result)