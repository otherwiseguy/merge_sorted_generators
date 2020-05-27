import unittest
import merge


class TestMergeIntersection(unittest.TestCase):
    def test_no_args(self):
        result = merge.merge_intersection()
        self.assertRaises(StopIteration, next, result)

    def test_single_empty_iterator(self):
        result = merge.merge_intersection(iter([]))
        self.assertRaises(StopIteration, next, result)

    def test_multiple_empty_iterator(self):
        result = merge.merge_intersection(iter([]), iter([]))
        self.assertRaises(StopIteration, next, result)

    def test_single_value_iterator(self):
        values = [1]
        result = merge.merge_intersection(iter(values))
        self.assertEqual(values[0], next(result))
        self.assertRaises(StopIteration, next, result)

    def test_single_matching_value(self):
        values = [[1], [1]]
        result = merge.merge_intersection(*(iter(v) for v in values))
        self.assertEqual(values[0][0], next(result))
        self.assertRaises(StopIteration, next, result)

    def test_two_matching_values(self):
        values = [[1, 2], [1, 2]]
        result = merge.merge_intersection(*(iter(v) for v in values))
        self.assertEqual(values[0][0], next(result))
        self.assertEqual(values[0][1], next(result))
        self.assertRaises(StopIteration, next, result)

    def test_no_overlapping_values(self):
        values = [[0, 1], [2, 3], [4, 5]]
        result = merge.merge_intersection(*(iter(v) for v in values))
        self.assertRaises(StopIteration, next, result)

    def test_proper_subset(self):
        values = [[0, 1, 2, 3, 4], [2, 3]]
        result = merge.merge_intersection(*(iter(v) for v in values))
        self.assertEqual(2, next(result))
        self.assertEqual(3, next(result))
        self.assertRaises(StopIteration, next, result)

    def test_intersecting_three(self):
        values = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = merge.merge_intersection(*(iter(v) for v in values))
        self.assertEqual(3, next(result))
        self.assertRaises(StopIteration, next, result)
