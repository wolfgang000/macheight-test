import unittest
import app

class TestApp(unittest.TestCase):
    def test_get_sorted_array_and_target_sum_from_input(self):
        input_1 = "1,9,5,0,20,-4,12,16,7" 
        input_2 = "12"
        (sorted_array, target_sum) = app.get_sorted_array_and_target_sum_from_input(input_1, input_2)
        self.assertEqual(sorted_array, [-4, 0, 1, 5, 7, 9, 12, 16, 20])
        self.assertEqual(target_sum, 12)


    def test_find_pairs(self):
        sorted_array = [-4, 0, 1, 5, 7, 9, 12, 16, 20]
        target_sum = 12
        pairs = app.find_pairs(sorted_array, target_sum)
        self.assertEqual(pairs, [(-4, 16), (0, 12), (5, 7)])


if __name__ == '__main__':
    unittest.main()