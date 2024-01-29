import unittest
from code.string_operations import StringOperations

class testStringOperations(unittest.TestCase):
    def setUp(self):
        self.str_op = StringOperations('arunisto')
    def test_reverse_string(self):
        self.assertEqual(self.str_op.reverse_string(),
                         'otsinura', "Failed")
    def test_upper_case(self):
        self.assertEqual(self.str_op.upper_case(),
                         'ARUNISTO', "Failed")
    def test_lower_case(self):
        self.assertEqual(self.str_op.lower_case(),
                         'arunisto', "Failed")

if __name__ == '__main__':
    unittest.main()
                         
