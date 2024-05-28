import unittest
from TestUtils import TestUtils

class BoundaryTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.test_obj = TestUtils()  # Initialize test_obj here

    def test_boundary(self):
        self.test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")

    def test_empty_string(self):
        my_string = ""
        self.test_obj.yakshaAssert(my_string[:3], "", "functional")

    def test_index_out_of_range(self):
        my_string = "Python"
        self.test_obj.yakshaAssert(my_string[20:], "", "functional")

    def test_negative_index_out_of_range(self):
        my_string = "Python"
        self.test_obj.yakshaAssert(my_string[-20:], "Python", "functional")

if __name__ == '__main__':
    unittest.main()
